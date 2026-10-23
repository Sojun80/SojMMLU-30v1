# SojMMLU-30 v2 — Challenge exam (questions only)



This is a **questions-only** packet. No answer key or scoring explanations are included.



**Instructions:** Answer all 30 multiple-choice questions. Do not browse or read other files in the repository. Return exactly one JSON object mapping question IDs to A–E letters (for example, `{"C01":"A","C02":"B"}`). Do not rely on a published key.



## C01 · Code & algorithms · moderate

What does this Python 3 program print?

```python
items = [[2], [3]]
shadow = items[:]
items[0].append(4)
shadow[1] = [5]
items.append(shadow[0])
print(sum(map(sum, items)), sum(map(sum, shadow)))
```

**A.** (15, 11)

**B.** (15, 9)

**C.** (12, 11)

**D.** (15, 15)

**E.** (9, 11)

## C02 · Code & algorithms · moderate

An SQL database has `accounts(id)` containing ids 1, 2, 3, 4 and `transactions(account_id, amount)` containing these rows:

| account_id | amount |
|---:|---:|
| 1 | 8 |
| 1 | -3 |
| 2 | NULL |
| 2 | 5 |
| 4 | -1 |

Under standard SQL NULL and LEFT JOIN semantics, which account IDs does this query return, in order?

```sql
SELECT a.id
FROM accounts AS a
LEFT JOIN transactions AS t ON a.id = t.account_id
GROUP BY a.id
HAVING COUNT(t.amount) >= 1
   AND COALESCE(SUM(t.amount), 0) > 0
ORDER BY a.id;
```

**A.** 1 only

**B.** 2 only

**C.** 1, 2, 3

**D.** 1, 2

**E.** 1, 2, 4

## C03 · Code & algorithms · hard

What does this Python 3 program print? The loop order matters.

```python
dp = [0] * 11
dp[0] = 1
for total in range(1, 11):
    for step in (2, 3, 5):
        if total >= step:
            dp[total] += dp[total - step]
print(dp[10])
```

**A.** 12

**B.** 14

**C.** 4

**D.** 8

**E.** 10

## C04 · Code & algorithms · hard

A cache with capacity 3 starts empty and uses exact least-recently-used (LRU) eviction. Every access (hit or miss) makes the accessed key most recently used; a miss inserts the key, evicting the least recently used one only when full.

For the sequence `A B C A D B E A C B`, how many misses occur?

**A.** 8

**B.** 10

**C.** 9

**D.** 6

**E.** 7

## C05 · Code & algorithms · challenge

Let n be an integer at least 2. Each call to `work()` takes constant time, and no loop is optimized away. What is the tight asymptotic running time of this pseudocode?

```text
i = 1
while i <= n:
    j = 1
    while j <= i:
        k = 1
        while k <= j:
            work()
            k = 2 * k
        j = 2 * j
    i = 2 * i
```

**A.** Theta(n)

**B.** Theta((log n)^3)

**C.** Theta(n log n)

**D.** Theta((log n)^4)

**E.** Theta((log n)^2)

## C06 · Code & algorithms · challenge

A directed graph has exactly these edges and positive integer weights:

| Edge | Weight | Edge | Weight |
|---|---:|---|---:|
| A -> B | 8 | B -> E | 6 |
| A -> C | 5 | C -> D | 11 |
| C -> B | 2 | D -> E | 3 |
| B -> D | 8 | D -> F | 11 |
| C -> F | 24 | E -> F | 5 |

You must travel from A to F. You may use **at most one coupon**, which replaces the cost of one traversed edge of weight w by floor(w/2). All other edges cost their listed weights. What is the minimum total cost?

**A.** 15

**B.** 13

**C.** 14

**D.** 16

**E.** 17

## M01 · Mathematics & quantitative reasoning · moderate

An urn contains 3 red and 5 blue balls. Three balls are drawn uniformly at random without replacement. Given that at least one drawn ball is red, what is the probability that exactly two are red?

**A.** 1/2

**B.** 15/56

**C.** 3/8

**D.** 5/14

**E.** 15/46

## M02 · Mathematics & quantitative reasoning · moderate

Two real numbers satisfy x+y=11 and xy=24. What is x^4+y^4?

**A.** 5329

**B.** 4105

**C.** 4176

**D.** 4177

**E.** 4225

## M03 · Mathematics & quantitative reasoning · hard

Two independent fair six-sided dice are rolled. Given that the **maximum** of the two results is exactly 5, what is the expected value of the **minimum** result?

**A.** 8/3

**B.** 3

**C.** 29/9

**D.** 25/9

**E.** 23/9

## M04 · Mathematics & quantitative reasoning · hard

A rectangle has positive side lengths x and y, with x+y=20 and x >= 2y. What is the maximum possible area xy?

**A.** 80

**B.** 800/9

**C.** 90

**D.** 100

**E.** 400/9

## M05 · Mathematics & quantitative reasoning · challenge

How many binary strings of length 12 contain **exactly four 1 bits** and have no adjacent 1 bits **when positions 12 and 1 are also considered adjacent**? Strings are distinguished by their numbered positions: rotations count as different strings.

**A.** 105

**B.** 126

**C.** 70

**D.** 84

**E.** 96

## M06 · Mathematics & quantitative reasoning · challenge

Starting at (0,0), a path takes only steps (1,0) and (0,1), ending at (6,5). It may never enter a point with y>x, and it **must pass through (3,2)**. How many distinct step sequences satisfy these conditions?

**A.** 60

**B.** 84

**C.** 42

**D.** 56

**E.** 70

## L01 · Logic & constraint solving · moderate

Exactly one of four boxes contains a coin. Each box bears a statement:

1. "The coin is in box 1."
2. "The coin is in box 2 or box 4."
3. "The coin is not in box 3."
4. "The coin is in box 1 or box 2."

Exactly **two** of these statements are true. Which box contains the coin?

**A.** Box 4

**B.** Box 2

**C.** Box 3

**D.** No box satisfies the rule

**E.** Box 1

## L02 · Logic & constraint solving · moderate

Every eligible applicant has a verified email or manager approval (possibly both). No contractor has manager approval. At least one contractor is eligible.

Which statement necessarily follows?

**A.** Every contractor is eligible.

**B.** No employee has manager approval.

**C.** All verified emails belong to contractors.

**D.** At least one eligible contractor has a verified email.

**E.** No eligible contractor exists.

## L03 · Logic & constraint solving · hard

Five distinct tasks A, B, C, D, E must be performed exactly once each. The order must satisfy all four rules:

- B occurs immediately before D.
- A occurs before C.
- D occurs before E.
- C is not last.

How many valid task orders exist?

**A.** 6

**B.** 1

**C.** 3

**D.** 2

**E.** 4

## L04 · Logic & constraint solving · hard

Four switches P, Q, R, S are ON or OFF. Exactly two are ON. All three constraints hold:

- If P is ON, then R is ON.
- If Q is ON, then R is OFF.
- S is ON **if and only if** exactly one of P and Q is ON.

Which pair of switches is ON?

**A.** Q and R

**B.** R and S

**C.** P and Q

**D.** P and R

**E.** Q and S

## L05 · Logic & constraint solving · challenge

Four people A, B, C, D are each either always truthful or always lying in their **single** statement. Their statements are:

- A: "B and C have the same truth status."
- B: "Exactly two of us are truthful."
- C: "D is lying."
- D: "A is lying."

Which pair is truthful?

**A.** A and C

**B.** B and C

**C.** B and D

**D.** C and D

**E.** A and B

## L06 · Logic & constraint solving · challenge

Six distinct tasks A, B, C, D, E, F must be performed in a single order. All constraints apply:

- A must precede B.
- C must occur immediately before D.
- E must not be first or last.
- F must occur after B.

How many of the 6! possible task orders satisfy every constraint?

**A.** 6

**B.** 8

**C.** 10

**D.** 16

**E.** 12

## S01 · Science & engineering · moderate

An ideal 12 V source powers a **2-ohm resistor in series** with a parallel pair of **3-ohm** and **6-ohm** resistors. What is the power dissipated in the 6-ohm resistor?

**A.** 12 W

**B.** 6 W

**C.** 3 W

**D.** 4 W

**E.** 8 W

## S02 · Science & engineering · moderate

The reaction is 2 Al + 3 Cl2 -> 2 AlCl3. Starting with 5 moles of aluminum and 6 moles of chlorine, with no other reactants, the process achieves a **75% yield** relative to its limiting reactant. How many moles of AlCl3 are actually produced?

**A.** 3.75

**B.** 4

**C.** 2

**D.** 3

**E.** 2.5

## S03 · Science & engineering · hard

A vehicle begins at rest, accelerates at a constant +2 m/s^2 for 5 seconds, then immediately brakes at -2.5 m/s^2 until it stops. Motion remains along a straight line without reversing. What total distance does it travel?

**A.** 45 m

**B.** 40 m

**C.** 50 m

**D.** 60 m

**E.** 35 m

## S04 · Science & engineering · hard

An insulated vessel contains **200 g of ice at 0 C**. Add **500 g of liquid water at 40 C**. Ignore vessel heat capacity and losses. Ice's latent heat of fusion is 334 J/g; liquid water's specific heat is 4.2 J/(g*C). After equilibrium, what is the final temperature, to two decimal places?

**A.** 0.00 C

**B.** 3.90 C

**C.** 8.00 C

**D.** 11.90 C

**E.** 5.85 C

## S05 · Science & engineering · challenge

A job originally requires exactly **100 seconds**: stage A takes 40 s, B takes 30 s, and C takes 30 s. A new system makes A 4 times faster and B 3 times faster, with C unchanged, **but adds 5 seconds of overhead** per job that did not exist before. The stages run sequentially. What is the overall speedup relative to the original 100-second job?

**A.** 5/2

**B.** 5/4

**C.** 20/11

**D.** 3/2

**E.** 2

## S06 · Science & engineering · challenge

A service needs a working shared power supply **and at least two working sensors** among A, B, C. The supply works with probability 0.95. Conditional on supply working, the three sensors work independently, with probabilities 0.9, 0.9, and 0.8 respectively. A supply failure makes the service fail regardless of sensors. What is the overall probability the service works?

**A.** 0.9500

**B.** 0.9063

**C.** 0.9540

**D.** 0.855

**E.** 0.9000

## E01 · Reading, evidence & interpretation · moderate

A binary classifier flags 50 items as positive. Of those 50, exactly 30 are truly positive. The evaluation dataset contains **200 actual positive items** in total. What are precision and recall, in that order?

**A.** 60% precision; 15% recall

**B.** 60% precision; 30% recall

**C.** 30% precision; 15% recall

**D.** 75% precision; 15% recall

**E.** 15% precision; 60% recall

## E02 · Reading, evidence & interpretation · moderate

An organization grants access **if and only if** all relevant conditions are satisfied:

- The applicant is either (a) an employee with manager approval or (b) a contractor with sponsor approval.
- Anyone accessing a confidential project must have completed security training.
- Suspended accounts never receive access.

Which applicant must receive access under these rules?

**A.** An active employee with manager approval seeking a confidential project, without training.

**B.** An active contractor with manager approval but no sponsor approval, seeking a nonconfidential project.

**C.** An active contractor with sponsor approval seeking a nonconfidential project.

**D.** An active employee with sponsor approval but no manager approval, seeking a nonconfidential project.

**E.** A suspended contractor with sponsor approval and training seeking a confidential project.

## E03 · Reading, evidence & interpretation · hard

A randomized study assigns **100** participants to treatment and **100** to control. In treatment, outcomes are observed for 80 participants, including 60 successes; 20 outcomes are missing. In control, outcomes are observed for 95 participants, including 60 successes; 5 outcomes are missing. Assume each missing outcome could independently be either success or failure.

Across **all randomized participants**, what is the tightest possible interval for treatment success rate minus control success rate, in **percentage points**?

**A.** -20 to +5

**B.** 0 to +20

**C.** -5 to +5

**D.** +5 to +20

**E.** -5 to +20

## E04 · Reading, evidence & interpretation · hard

An audit establishes these facts:

1. Every server that sent a heartbeat was online at noon.
2. Every server online at noon had **either** completed patching **or** was behind an isolation proxy (possibly both).
3. No server behind an isolation proxy accepted public traffic.
4. At least one server that sent a heartbeat accepted public traffic.

Which conclusion necessarily follows?

**A.** Every patched server sent a heartbeat.

**B.** Every online server accepted public traffic.

**C.** Every server completed patching.

**D.** At least one server that sent a heartbeat completed patching.

**E.** No server used an isolation proxy.

## E05 · Reading, evidence & interpretation · challenge

A security threat is present on **5%** of occasions. A detector triggers an alert with **80% sensitivity**, and triggers a false alert on **10%** of threat-free occasions.

After an alert, there are two actions. **Intervene** costs 2 units if there is no threat and 0 if there is a threat. **Do not intervene** costs 7 units if there is a threat and 0 otherwise. Select the action with the lower expected cost.

Which pair gives the correct action and the probability of a real threat given the alert?

**A.** Do not intervene; 8/27

**B.** Intervene; 8/27

**C.** Intervene; 2/5

**D.** Do not intervene; 2/5

**E.** Intervene; 4/27

## E06 · Reading, evidence & interpretation · challenge

Two classifiers were evaluated on a test population containing 90% group A and 10% group B, but the **deployment** population will contain 70% A and 30% B.

Their group-specific error rates, assumed unchanged at deployment, are:

| Model | Group A error | Group B error |
|---|---:|---:|
| X | 2% | 20% |
| Y | 5% | 10% |

Which model has lower expected error in deployment, and by how many **percentage points**?

**A.** X by 1.7 points

**B.** X by 0.9 points

**C.** Y by 0.9 points

**D.** Y by 1.7 points

**E.** They tie
