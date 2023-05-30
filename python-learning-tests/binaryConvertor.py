
class Convert:

    @staticmethod
    def int_to_binary(num):
        list = []
        while num >= 1:
            list.append(num % 2)
            num = num / 2
            num = int(num)
        return list[::-1]

    @staticmethod
    def binary_to_int(list):
        num = 0
        track = 0
        for i in list:
            if (i == 1):
                num = num + 2 ** track
            else:
                num += 0
            track += 1   
        return num       

print(Convert.int_to_binary(357))
list = [1, 0, 1, 1, 0, 0, 1, 0, 1]

print(Convert.binary_to_int(list[::-1]))