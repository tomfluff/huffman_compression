import text_gen
import huffman
import math

N = 500

def kl_divergence(prob_p:dict, prob_q:dict):
    # p is ACTUAL propability, q is ASSUMED probability
    kl = 0
    for x in prob_p.keys():
        assert x in prob_q
        kl += prob_p[x] * math.log(prob_p[x] / prob_q[x], 2)
    return kl

def compression_ratio(text:str, codes:dict):
    bit_num_normal = len(text)*8
    bit_num_compressed = 0
    for c in text:
        assert c in codes
        bit_num_compressed += len(codes[c])
    return (bit_num_normal, bit_num_compressed)

if __name__ == "__main__":
    # generate text A
    G_a = text_gen.TextGen({'A':0.3,'B':0.2,'C':0.15,'D':0.25,'E':0.1})
    T_a = G_a.generate(N)
    # generate text B
    G_b = text_gen.TextGen({'A':0.02,'B':0.25,'C':0.1,'D':0.05,'E':0.58})
    T_b = G_b.generate(N)

    C_a = dict(huffman.calculate_huffman_codes(huffman.build_huffman_tree(T_a)))
    C_b = dict(huffman.calculate_huffman_codes(huffman.build_huffman_tree(T_b)))

    pq_A = huffman.get_symbols_freq(T_a)
    pq_B = huffman.get_symbols_freq(T_b)

    # KL Divergence
    print(f"P:= Text A, Q:= Text A : KL={kl_divergence(G_a.alphabet, pq_A)}")
    print(f"P:= Text A, Q:= Text B : KL={kl_divergence(G_a.alphabet, pq_B)}")
    print(f"P:= Text B, Q:= Text A : KL={kl_divergence(G_b.alphabet, pq_A)}")
    print(f"P:= Text B, Q:= Text B : KL={kl_divergence(G_b.alphabet, pq_B)}")

    # Compress text_a with compressor_a
    _notm_bit,_comp_bit = compression_ratio(T_a,C_a)
    print(f"Text A (Compressor A) : ratio={_comp_bit/_notm_bit} ({_comp_bit} / {_notm_bit})")
    # Compress text_a with compressor_b
    _notm_bit,_comp_bit = compression_ratio(T_a,C_b)
    print(f"Text A (Compressor B) : ratio={_comp_bit/_notm_bit} ({_comp_bit} / {_notm_bit})")

    # Compress text_b with compressor_a
    _notm_bit,_comp_bit = compression_ratio(T_b,C_a)
    print(f"Text B (Compressor A) : ratio={_comp_bit/_notm_bit} ({_comp_bit} / {_notm_bit})")
    # Compress text_b with compressor_b
    _notm_bit,_comp_bit = compression_ratio(T_b,C_b)
    print(f"Text B  (Compressor B) : ratio={_comp_bit/_notm_bit} ({_comp_bit} / {_notm_bit})")
    