boxes = ["1.door.txt", "2.window.txt", "3.ball.txt"]
for box in boxes:
# check on console that if box [1] gives the " . ", as box in boxes is 1 element, and in consist itself of 1 . door . txt , so 0 = "1", 1= ".",2 = "door" etc
box[1] = "_"
# if we want to replace "." to "_" , we can not use above code as the str is immutable , str don't not support item assignment, but lists are mutable
boxex[1] = 1.write.txt
# this will give you an output that will change the 1st item in the list 
box.replace(".", "_")
# '1_door_txt'  this is the output
#do not forget to store it, otherwise it will just show the output
box = box.replace(".", "_")
print(box)

#tuples  same as list but with () and are immutable 
