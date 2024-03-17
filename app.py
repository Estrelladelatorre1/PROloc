from flask import Flask, request, render_template

app = Flask(__name__)

def perezosa(a,b):
        def sum(a, b):
            return a + b
            
        result = sum(a, b)
        return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculateFuncionesPuras', methods=['POST'])
def calculateFuncionesPuras():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
            operation_sign = '+'
        elif operation == 'subtract':
            result = num1 - num2
            operation_sign = '-'
        elif operation == 'multiply':
            result = num1 * num2
            operation_sign = '×'
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
                operation_sign = '÷'
            else:
                return "Cannot divide by zero!"
        else:
            return "Invalid operation"

        return render_template('result.html', num1=num1, num2=num2, operation_sign=operation_sign, result=result)


@app.route('/calculateFuncionesDeOrdenSuperior', methods=['POST'])
def calculateFuncionesDeOrdenSuperior():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
            operation_sign = 'add'
        elif operation == 'subtract':
            result = num1 - num2
            operation_sign = 'subtract'
        elif operation == 'multiply':
            result = num1 * num2
            operation_sign = 'multiply'
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
                operation_sign = 'divide'
            else:
                return "Cannot divide by zero!"
        else:
            return "Invalid operation"

        return render_template('result.html', num1=num1, num2=num2, operation_sign=operation_sign, result=result)

@app.route('/calculateIntervalos', methods=['POST'])
def calculateIntervalos():
    if request.method == 'POST':
        print("Calculando intervalos...")
        def inclusive_range(start, end):
            return list(range(start, end + 1))

        def exclusive_range(start, end):
            return list(range(start, end))

        # Ejemplo de uso
        start = int(request.form['num1'])
        end = int(request.form['num2'])

        inclusive_result = inclusive_range(start, end)
        exclusive_result = exclusive_range(start, end)

        print("Intervalo inclusivo:", inclusive_result)
        print("Intervalo exclusivo:", exclusive_result)        
        return render_template('result.html', num1="", num2=inclusive_result, operation_sign="=", result=exclusive_result)
    
@app.route('/calculateOperadores', methods=['POST'])
def calculateOperadores():
    if request.method == 'POST':
        equal_to = lambda x, y: x == y
        not_equal_to = lambda x, y: x != y
        greater_than = lambda x, y: x > y
        less_than = lambda x, y: x < y
        greater_than_or_equal = lambda x, y: x >= y
        less_than_or_equal = lambda x, y: x <= y

        # Ejemplo de uso de las funciones lambda
        x = int(request.form['num1'])        
        y = int(request.form['num2'])

        # Definir funciones lambda para operadores lógicos
        logical_and = lambda x, y: x and y
        logical_or = lambda x, y: x or y
        logical_not = lambda x: not x

        # Ejemplo de uso de las funciones lambda para operadores lógicos
        a = True
        b = False

        result = "Igual a: " + str(equal_to(x, y)) + "\n"
        result += "Diferente de: " + str(not_equal_to(x, y)) + "\n"
        result += "Mayor que: " + str(greater_than(x, y)) + "\n"
        result += "Menor que: " + str(less_than(x, y)) + "\n"
        result += "Mayor o igual que: " + str(greater_than_or_equal(x, y)) + "\n"
        result += "Menor o igual que: " + str(less_than_or_equal(x, y)) + "\n"
        result += "AND lógico: " + str(logical_and(a, b)) + "\n"
        result += "OR lógico: " + str(logical_or(a, b)) + "\n"
        result += "NOT lógico de 'a': " + str(logical_not(a)) + "\n"
        result += "NOT lógico de 'b': " + str(logical_not(b)) + "\n"

        return render_template('result.html', num1="", num2="resultado", operation_sign="=", result=result)
    
@app.route('/calculateAplicacionesDeLasListas', methods=['POST'])
def calculateAplicacionesDeLasListas():
    if request.method == 'POST':
        def stringToList(string):
            return [int(item) for item in string.split(',')]    
        list = stringToList(request.form['num1'])
        return render_template('result.html', num1="", num2="resultado", operation_sign="=", result=list)
    
@app.route('/calculateArbol', methods=['POST'])
def calculateArbol():
    if request.method == 'POST':
        def stringToList(string):
            return [int(item) for item in string.split(',')]    
        list = stringToList(request.form['num1'])
        # Organizar la lista de números de mayor a menor
        numeros_ordenados = sorted(list, reverse=True)

        return render_template('result.html', num1="", num2="resultado", operation_sign="=", result=numeros_ordenados)
    
@app.route('/calculateEvPerezosa', methods=['POST'])
def calculateEvPerezosa():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = perezosa(num1, num2)
        return render_template('result.html', num1="", num2="resultado", operation_sign="=", result=result)

if __name__ == '__main__':
    app.run(debug=True)
