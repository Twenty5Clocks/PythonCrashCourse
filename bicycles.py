#Jeremy 20210606
#Showcasing lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#accessing elements of the list
print(bicycles[0])
print(bicycles[0].title())
#index positions start at 0 not 1

print(bicycles[1])
print(bicycles[3])

#last item in list using -1
print(bicycles[-1])


message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)