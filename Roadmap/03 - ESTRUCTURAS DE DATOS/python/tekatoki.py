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
    ex_tuple:tuple[int] = (23, 51, 24)
    ex_set:set[float] = {73.0, 3.4, 3.1415}
    ex_dict:dict = {'name': 'Jack', 'lastname': 'Bluepark', 'age': 21}

    print(ex_list, ex_tuple, ex_set, ex_dict)

    # List's methods
    ex_list.append('ok')
    print(f'Append method [list] > {ex_list}')

    ex_list.extend(['nothing', 'xz', 'mathematics are sexy'])
    print(f'Extend method [list] > {ex_list}')

    ex_list.insert(3, 'maboy')
    print(f'Insert method [list] > {ex_list}')

    ex_list.remove('2')
    print(f'Remove method [list] > {ex_list}')
    
    ex_list.pop(2)
    print(f'Pop method [list] > {ex_list}')

    ex_list.clear()
    print(f'Clear method [list] > {ex_list}')

    ex_list.extend(['nothing', 'xz', 'mathematics are sexy'])
    print(f'Added things to clear list > {ex_list}')

    ex_list.sort()
    print(f'Sort method [list]> {ex_list}')

    ex_list.reverse()
    print(f'Reverse method [list] > {ex_list}')
    

def chose_function(function_1, function_2, key_function:int=0)-> None:
    if 0 == key_function:
        function_1()
    elif 1 == key_function:
        function_2()
    else:
        print('Introduce a valid key value <in range 0,1>')


def main()->None:
    in_user:int = int(input('Print [0, 1] >'))
    chose_function(simple_exercise, None, in_user)

if __name__ == '__main__':
    main()
