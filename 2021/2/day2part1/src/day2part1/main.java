package day2part1;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;




public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int depth = 0;
		int hor = 0;
		
		try {
			File inputdata = new File("input.txt");
			Scanner myReader = new Scanner(inputdata);
			while (myReader.hasNextLine()) {
				String data = myReader.nextLine();
				// split array into 2 parts command and value
				String[] splited = data.split("\\s+");
				System.out.println(splited[0]);
				int dir_val = Integer.parseInt(splited[1]);
				System.out.println(dir_val);
				// create an if statement to determine where to add/subtract values from
				if (splited[0].equals("forward")) {
					System.out.println(splited[0].equals("forward"));
					int x = splited[0].equals("forward") ? 1:0;
					System.out.println(x);
					
					hor += dir_val;
				} else {
//					System.out.println("Else Statement");
					depth += dir_val*(splited[0].equals("down") ? 1:0) - dir_val*(splited[0].equals("up") ? 1:0);
				}
				
				
			}
			myReader.close();
		} catch (FileNotFoundException e) {
			System.out.println("An error occured.");
			e.printStackTrace();
		}
		
		System.out.println(hor);
		System.out.println(depth);
		System.out.println(depth*hor);
		System.out.println("Completed");
	}

}

