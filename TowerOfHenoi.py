def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)


# Driver code
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
exit()
n=int(input("No of blocks: "))

def TowerOfHenoi(n,BEG,DIST):
    AUX='B'
    if n==1:
        print(f"{n} disk moves from {BEG} to {DIST}")
        return
    TowerOfHenoi(n - 1, BEG,AUX)
    print(f"{n} disk moves from {BEG} to {DIST}")
    TowerOfHenoi(n-1,AUX,DIST)
TowerOfHenoi(n,'A','C')