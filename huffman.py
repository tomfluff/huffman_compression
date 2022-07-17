
class Huff_Node:
    def __init__(self, symbol, p, left=None, right=None) -> None:
       self.code = '' # will get 0 or 1
       self.symbol = symbol
       self.p = p #probability
       self.left = left
       self.right = right   
    
    def __repr__(self) -> str:
        return f"[{self.symbol}, {self.p} := {self.code}]"

def get_symbols_freq(text: str):
    out = {}
    for _c in text:
        if _c in out:
            out[_c] += 1
        else:
            out[_c] = 1.0
    for _c in out.keys():
        out[_c] /= len(text)
    return out

def build_huffman_tree(text):
    sym_freq = get_symbols_freq(text=text).items()
    assert len(sym_freq) >= 2 #at least two symbols in alphabet

    nodes = [Huff_Node(x[0],x[1]) for x in sym_freq]
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.p, reverse=True)

        _l = nodes.pop()
        _r = nodes.pop()
        _l.code = 0
        _r.code = 1
        
        nodes.append(Huff_Node(_l.symbol+_r.symbol, _l.p+_r.p, _l, _r))
    assert len(nodes) == 1
    return nodes[0] # returns the root of the huffman tree

def append_all(l1, l2):
    for e in l2:
        l1.append(e)
    return l1

def calculate_huffman_codes(node:Huff_Node, c=''):
    codes = []
    new_c = c+str(node.code)
    if node.left:
        codes = append_all(codes, calculate_huffman_codes(node.left,new_c))
    if node.right:
        codes = append_all(codes, calculate_huffman_codes(node.right,new_c))
    
    if not node.left and not node.right:
        codes.append((node.symbol,new_c))
        return codes
    
    return codes