
#About Hashing
'''

Symbole-table problem:
Table S, holds in records

key
+
Satellite data

Operations we want to do:

    Dynamic Op  Insert(S,x): S <- S u {x}
    Dynamic Op  Delete(S,x): S <- S - {x}
    Static  Op  Search(S,x): return x $ key[x]=k or nil if no such x

Simple implementation: direct access table
    Works if: keys are drawn from U={0,1,...,n-1}, keys are distinct.

    Set up array T[0,...,m-1] to represent dynamic set S such as:
            T[k] = x if x in S and key[x]=k, nil otherwise
            Ops take constant time : O(1)
    Drawback: m-1 can be a huge number
Hashing:
    Assumption: Hash function h maps keys 'randomly' into slots of table T

    hash(x)=hash(y) -> collusion
    when a record to be inserted maps to an already occupied slot, a collusion
    occurs.
    Resolving collision by chaining -> link records in the same slot into a list
    ie hash(49) = hash(46) = i

    Worst Case:
        Every key hashes to the same slot -> Access takes O(n) time
    Average Case:
        Assumption of simple uniform hashing.
         --> Each key k in S is equally likely to be hashed to any slot in T,
         independently of where other records are hashed.
        Probability that to keys are hashed to the same slot: 1/m

def The low factor of a hash table with n keys and m slots to be alpha = n/m
alpha is the average number of keys per slot.

    The expected unsuccessful search time is O(1+ alpha)

        expect search time =O(1) if alpha=O(1) <-> n = O(m)
        <-> number of elements in the table is upper-bounded by X*m
        if hash table is smaller than the number of elements, the search time will
        grow as m doesn't keep up with n. (ie. n/m not constant)

    The expected successful search time is also O(1+ alpha)

        -->  Operations of constant time.

In choosing a hash function, we would like it to distribute keys uniformly into slots
and regularity in the key distribution should not effect uniformity.

Quick hash function exemple: Division method
    let hash(k) = k[m]
    careful: Don't pick m with small diviser d, generally m to be a large prime not
    too close to a power of 2 or 10.

    But divisions tend to take lots of cycle on computers -> not a very good method

Quick hash function exemple: Multiplication method
    Assumptions: m = 2^r, computer has w-bit words.
    hash(k)=a*k [2^ w] bit wise right shifted by (w - r)
    k is an odd integer in [2^(w-1), 2^(w)]

    Don't pick A too close to a power of 2 and generaly a fast method because multiplicatipn
    and right shift are fast.



A fundamental weakness of hashing : for any hash function, there exist a bad set of keys all hashed to the same slot.

'''

#About Time Stamping
#About Networks
#About ICO

