import ast, sys
import os
from os import system
from firebase_admin import db

# class NodeVisitor(ast.NodeVisitor):
#     def visit_Str(self, tree_node):
#         print('{}'.format(tree_node.s))
    
    # def visit_Call(self, node: Call) -> Any:
    #     return super().visit_Call(node)





class NodeTransformer(ast.NodeTransformer):
    def visit_Str(self, tree_node):
        return ast.Str('String: ' + tree_node.s)
    
    def visit_Call(self, node: ast.Call):
        # print(ast.dump(ast.parse(node)))
        self.generic_visit(node)
        # print(node.func.id)
        tempered_node = node
        if node.func.id == 'input':
            # print('ur being hacked')    
            tempered_node = ast.Call(func=ast.Name(id='my_function', ctx=ast.Load()), args=[node], keywords=[])
        # print('\n'*3)
        return tempered_node    
        # return node






if __name__ == "__main__":

    fileName = sys.argv[1]


    
    with open(f"./{fileName}") as sample:
        data = sample.read()
        # print(ast.dump(ast.parse(data)))
        tree = NodeTransformer().visit(ast.parse(data))
        # print(ast.dump(tree))
        # print(ast.unparse(tree))
        with open(f"./{fileName}x", "w") as output:
            output.write(
'''
import firebase_admin
from firebase_admin import db

def setup_firebase():
    cred_obj = firebase_admin.credentials.Certificate('./results/python-collector-firebase-adminsdk-2uy87-fb30db032c.json')
    default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://python-collector-default-rtdb.asia-southeast1.firebasedatabase.app/'
	})
def my_function(inp):
    ref = db.reference("/")
    ref.push(inp)
    return inp

setup_firebase()
''')
            output.write(ast.unparse(tree))
            # system('')
        with open(f"./{fileName}x", "r") as output:
            # print('---------------')
            lines = [line.rstrip('\n\r') for line in output.readlines()]
            lines.pop(0)
            # print('\n'.join(lines))
            exec('\n'.join(lines))
        os.remove(f'{fileName}x')
            # eval(''.join(output.readlines()))
            # print("done executing")            
        
        



    