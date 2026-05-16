# generators
# -----------
# generator in python is enable lazy evolution for producing sequence of values effeciently
# they actually differ from functions by execution and resuming on demand
# generators create iterators yield values one at time using the yield keyword

# difference blw functions and generators

# regular functions execute only fully upon call and return a single value and terminating afterward(one calling function only for one use)
# generaators use yield to produce multiple values lazily,it acts like itertors without building the entire sequence in memory
# def gen_(num):
#     count=0
#     i=1
#     while i<=num:
#         yield i
#         i+=1
# gen1_=gen_((3))
# print(next(gen1_))
# print(next(gen1_))
# print(next(gen1_))


#yield
#---------
#yield pauses the generator function saves its state (local variable,position and returns the yield value) to the caller


#next
#--------
#this advances the generator by executing until the next yield returning that value,subsequently calls resume from there 
def gen_():
    yield "First msg"
    yield "Second msg"
    yield "Third msg"
gen1_=gen_()
print(next(gen1_))
print(next(gen1_))
print(next(gen1_))