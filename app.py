def get_operators_and_examples():
    operators = {
        'Operadores Aritméticos': ['+', '-', '*', '/', '%', '**'],
        'Operadores de Comparación': ['==', '!=', '>', '<', '>=', '<='],
        'Operadores Lógicos': ['&&', '||', '!'],
        'Operadores de Asignación': ['=', '+=', '-=', '*=', '/=', '%=', '**='],
        'Operadores de Rango': ['..', '...']
    }

    tree_example = """
    tree = {
        value: 10,
        left: {
            value: 5,
            left: nil,
            right: nil
        },
        right: {
            value: 15,
            left: nil,
            right: nil
        }
    }
    """

    inclusive_range_example = "(1..10).to_a  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
    exclusive_range_example = "(1...10).to_a  # [1, 2, 3, 4, 5, 6, 7, 8, 9]"

    return operators, tree_example, inclusive_range_example, exclusive_range_example
