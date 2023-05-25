
#! Convert a integer into a roman number and vice verse
#! Using OOP

#! Input:

#* 4456 / MMMMCDLVI

#! Output:

#* MMMMCDLVI / 4456 

#! Code goes here:

class convert:
    def int_to_roman(self, num):

        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
        syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman = ''
        list = 0
        times = 0
        final = ''
        while num > 0:
            for i in val:
                if (num // i) != 0:
                    roman = syb[list]
                    times = num // i

                    num = num % i

                    final += roman * times
                
                list += 1
            return final

        if num == 0:
            return("There is no '0' in roman numbers!! Go study!")
        
        if num < 0:
            return("There are no negatives in roman numbers!! Go study!")

    



                    
                    



number = int(input("Enter a integer number to convert it to roman number! -->"))
converting = convert().int_to_roman(number)
print(converting)

