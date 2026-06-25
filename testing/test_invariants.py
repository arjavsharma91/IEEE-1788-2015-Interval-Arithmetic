import re
from gmpy2 import mpfr
from intervals.decorated_interval import DecoratedInterval

def run_itf_line(itf_line: str):
    """Parses and executes a single plain text string line from an ITF test file.
    Supports primitives, metrics, relations, and transcendental functions.
    """
    # 1. Clean line and ignore comments/blank lines
    itf_line = itf_line.strip()
    if not itf_line or itf_line.startswith("#") or "->" not in itf_line:
        return True
        
    if itf_line.endswith(";"):
        itf_line = itf_line[:-1]

    # Pattern capture for: op_name( arguments ) -> expected_target
    match = re.match(r"^\w+\s*=\s*(\w+)\s*\((.+)\)\s*->\s*(.+)$", itf_line)
    if not match:
        match = re.match(r"^(\w+)\s*\((.+)\)\s*->\s*(.+)$", itf_line)
        
    if not match:
        raise ValueError(f"Malformed ITF string syntax rules broken: {itf_line}")

    op_name = match.group(1).lower().strip()
    args_str = match.group(2).strip()
    expected_str = match.group(3).lower().strip()

    # 2. Parse inputs cleanly without breaking inner interval bounding coordinates
    raw_args = re.split(r",(?![^\[]*\])", args_str)
    operands = []
    for arg in raw_args:
        arg = arg.strip()
        # If argument is a plain scalar number (like the second argument in some power/scalar functions)
        if not arg.startswith("[") and not arg.endswith("]") and "_" not in arg and arg not in ("nai", "empty"):
            operands.append(mpfr(arg))
        else:
            operands.append(DecoratedInterval.from_string(arg))

    # 3. Dynamic Execution Router
    # Primitives
    if op_name == "add":
        result = operands[0] + operands[1]
    elif op_name == "sub":
        result = operands[0] - operands[1]
    elif op_name == "mul":
        result = operands[0] * operands[1]
    elif op_name == "div":
        result = operands[0] / operands[1]
        
    # Metrics (Properties returning a scalar/mpfr)
    elif op_name in ("width", "radius", "midpoint", "magnitude", "mignitude"):
        result = getattr(operands[0], op_name)
        
    # Metrics requiring two intervals (Bound distances)
    elif op_name in ("inf_sub", "sup_sub"):
        result = getattr(operands[0], op_name)(operands[1])
        
    # Set Relations (Returning boolean values)
    elif op_name in ("subset", "proper_subset", "overlaps", "disjoint", "precedes", "meets"):
        result = getattr(operands[0], op_name)(operands[1])
        
    # Transcendental Functions (sin, cos, exp, log, atanh, etc.)
    else:
        import intervals.functions as funcs  
        if hasattr(funcs, op_name):
            func_to_call = getattr(funcs, op_name)
            if op_name == "atan2":
                result = func_to_call(operands[0], operands[1])
            else:
                result = func_to_call(operands[0])
        else:
            raise NotImplementedError(f"Operation handling framework for '{op_name}' not wired yet.")

    # 4. Validation and Evaluation Layer
    # Case A: Expected output is a boolean relation (true/false)
    if expected_str in ("true", "false"):
        assert result == (expected_str == "true"), f"ITF Mismatch ({op_name}): Expected {expected_str}, got {result}"
        
    # Case B: Expected output is a number scalar (for set metrics like width/radius)
    elif isinstance(result, mpfr):
        expected_num = mpfr(expected_str)
        if expected_num.isnan():
            assert result.isnan(), f"ITF Metric Mismatch: Expected NaN, got {result}"
        else:
            assert result == expected_num, f"ITF Metric Mismatch: Expected {expected_num}, got {result}"

    # Case C: Expected output is a standard DecoratedInterval
    else:
        expected_interval = DecoratedInterval.from_string(expected_str)
        
        # Core basic primitives demand strict bitwise equality
        if op_name in ("add", "sub", "mul", "div"):
            assert result == expected_interval, f"ITF State Mismatch ({op_name}): Expected {expected_interval}, got {result}"
        
        # Transcendental functions fall back to strict mathematical subset containment
        else:
            if expected_interval.is_nai:
                assert result.is_nai, f"Expected NaI for {op_name}, but got {result}"
            else:
                # Check that decorations match or degraded safely
                assert result.decoration <= expected_interval.decoration, \
                    f"Decoration leak in {op_name}: Expected {expected_interval.decoration}, got {result.decoration}"
                
                # Check strict enclosure (calculated interval must cover the expected one)
                assert expected_interval.interval.subset(result.interval), \
                    f"Containment violation in {op_name}!\nExpected (ITF): {expected_interval}\nCalculated (Ours): {result}"
                    
    return True


def test_via_itf_file(file_path: str):
    """Consumes an external plain text file to track and execute a linear batch runner loop."""
    with open(file_path, "r") as f:
        for line_num, line in enumerate(f, 1):
            try:
                run_itf_line(line)
            except AssertionError as e:
                print(f"❌ Verification crash on file line {line_num}: {line.strip()}")
                raise e
    print(f"✅ Integrated test compilation file '{file_path}' passed cleanly.")
