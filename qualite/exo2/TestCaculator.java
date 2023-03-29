package exo2;

public class TestCaculator {

	public static void main(String[] args) {

		Calculator calc=new Calculator();
		CalculatorOperation op=new Addition(2,3);
		CalculatorOperation op2 = new Substraction(3,2);
		calc.calculate(op2);
		calc.calculate(op);

		System.out.println("test addition");
		System.out.println((int) op.getResult() == 5);
		System.out.println("Test soustraction ");
		System.out.println((int) op2.getResult() == 1);
	}

}
