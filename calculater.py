Step 1: Define operation functions
DEFINE function add(a, b)
    RETURN a + b

DEFINE function subtract(a, b)
    RETURN a - b

DEFINE function multiply(a, b)
    RETURN a * b

DEFINE function divide(a, b)
    Ensure that b is not zero when calling
    IF b == 0 THEN
        PRINT "Error: Division by zero is not allowed."
        RETURN None
    END IF
    RETURN a / b
Step 2: Map operations to functions in a dictionary
SET operations = { "+": add, "-": subtract, "*": multiply, "/": divide }

Step 3: Get user input
PRINT "Enter the first number:"
SET first_number = USER_INPUT
PRINT "Enter the second number:"
SET second_number = USER_INPUT
PRINT "Enter the operation (+, -, *, /):"
SET operation = USER_INPUT

Step 4: Perform the operation using the dictionary
IF operation IN operations THEN
    SET result = operations[operation](first_number, second_number)
    
    Check for None result (in case of division by zero)
    IF result IS NOT None THEN
        Step 5: Display the result
        PRINT "The result of", first_number, operation, second_number, "is", result
    END IF
ELSE
    PRINT "Error: Invalid operation."
END IF


