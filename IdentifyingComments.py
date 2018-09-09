import re


def identify_comments(text):
    regex = "(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)"
    match = re.findall(regex, text)
    result = ""
    for line in match:
        for val in line:
            val = val.strip()
            if val and val[0] == "/":
                result += val.strip() + "\n"

    print(result)


if __name__ == "__main__":
    text = """/*This is a program to calculate area of a circle after getting the radius as input from the user*/  
        #include <stdio.h>
        int main()  
        {
           double radius,area;//variables for storing radius and area  
           printf("Enter the radius of the circle whose area is to be calculated\n");  
           scanf("%lf",&radius);//entering the value for radius of the circle as float data type  
           area=(22.0/7.0)*pow(radius,2);//Mathematical function pow is used to calculate square of radius  
           printf("The area of the circle is %lf",area);//displaying the results  
        }  
        /*A test run for the program was carried out and following output was observed  
        If 50 is the radius of the circle whose area is to be calculated
        The area of the circle is 7857.1429*/
        """

    identify_comments(text)
