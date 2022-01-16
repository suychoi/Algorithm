print("\    /\\\n" + " )  ( \')\n" + "(  /  )\n" + " \(__)|\n")
print("|\_/|\n" + "|q p|   /}\n" + "( 0 )\"\"\"\\\n" + "|\"^\"`    |\n" + "||_/=\\\\__|")

a, b = input().split()
print(int(a) + int(b))
print(int(a) - int(b))
print(int(a) * int(b))
print(int(int(a) / int(b)))
print(int(a) % int(b))

A, B, C = input().split()
print((int(A) + int(B))%int(C))
print(((int(A) % int(C)) + (int(B) % int(C))) % int(C))
print((int(A) * int(B))%int(C))
print(((int(A) % int(C)) * (int(B) % int(C))) % int(C))

A = int(input())
B = input()
print(int(B[2]) * A)
print(int(B[1]) * A)
print(int(B[0]) * A)
print((int(B[0]) * A)*100 + (int(B[1]) * A) * 10 + (int(B[2]) * A))

