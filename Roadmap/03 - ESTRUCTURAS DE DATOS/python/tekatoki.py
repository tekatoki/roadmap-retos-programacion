'''
╔═══════════════════════════════════════╗
║ Autor:  tekatoki                      ║
║ GitHub: https://github.com/tekatoki   ║
║ 2024 -  Python                        ║
╚═══════════════════════════════════════╝

Exercise:
- Show examples of the creation of all structures supported
by default in your language.
- Use operation of insertions, earase, update, sort.

Difficulty extra (optional):

Create a contacts agenda on the terminal
- Must implement fucnctionality of search, insection, update and 
delete contacts
- Each contact must have a name and a telephone number
- The pogram ask the first place what is the operation to be done and then
ask the necessary data
- The program mustn't let the user introduce telephone numbers no numeric or with
more than 11 digits. 
- You must put an operation that finish the program
'''


def simple_exercise()->None:
    ex_list:list[str] = ['h', '2', 'hi']
    ex_tuple:tuple[int] = [23, 51, 24]
    ex_set:set[float] = {73.0, 3.4, 3.1415}
    ex_dict:dict = {'name': 'Jack', 'lastname': 'Bluepark', 'age': 21}

def chose_function(function_1:function, function_2:function, key_function:int=0)-> None:
    if 0 == key_function:
        function_1()
    elif 1 == key_function:
        function_2()
    else:
        print('Introduce a valid key value <in range 0,1>')


def main()->None:
    print()

if __name__ == '__main__':
    main()
