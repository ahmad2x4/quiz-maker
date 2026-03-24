---
id: statistics-data-analysis-chapter-9-001
title: "Data Analysis Chapter 9: Analysing Data"
topic: statistics
difficulty: medium
questionCount: 20
createdFrom: "Chapter 9 Data Analysis.pdf"
dateGenerated: "2026-03-23"
estimatedTime: 30
tags: ["mean", "median", "mode", "range", "outlier", "histogram", "stem-and-leaf", "distribution", "skewness", "sampling", "categorical-data", "numerical-data"]
description: "Covers Year 9 Statistics Chapter 9: measures of centre and spread, histograms, stem-and-leaf plots, distribution shape, comparing data sets, and types of data."
---

# Data Analysis Chapter 9: Analysing Data

## Question 1

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

The maximum daily temperatures (°C) in Sydney over a fortnight in March were:

$$34,\ 22,\ 32,\ 26,\ 23,\ 24,\ 24,\ 26,\ 31,\ 26,\ 27,\ 28,\ 28,\ 27$$

What is the mean temperature? (Round to one decimal place if needed.)

**Options:**
- A) $26.5$°C
- B) $27.0$°C
- C) $26.0$°C
- D) $28.0$°C

<details>
<summary>Show Explanation</summary>

### Solution

Sum all values, then divide by the number of values ($n = 14$):

$$\bar{x} = \frac{34+22+32+26+23+24+24+26+31+26+27+28+28+27}{14} = \frac{378}{14} = 27$$

</details>

---

## Question 2

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

Using the same Sydney temperature data from Question 1, what is the **median** temperature?

$$22,\ 23,\ 24,\ 24,\ 26,\ 26,\ 26,\ 27,\ 27,\ 28,\ 28,\ 31,\ 32,\ 34$$

**Options:**
- A) $27.0$°C
- B) $26.0$°C
- C) $26.5$°C
- D) $27.5$°C

<details>
<summary>Show Explanation</summary>
**Correct Answer: C) $26.5$°C**


### Solution

Arrange the 14 values in order (already shown). With an even number of values, the median is the **average of the 7th and 8th values**:

- 7th value: $26$
- 8th value: $27$

$$\text{Median} = \frac{26 + 27}{2} = 26.5 \text{°C}$$

</details>

---

## Question 3

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

Year 9 students received the following speech scores (out of 10). Use the frequency table to calculate the mean score.

| Score ($x$) | Frequency ($f$) |
|:-----------:|:---------------:|
| 3 | 2 |
| 4 | 5 |
| 5 | 10 |
| 6 | 36 |
| 7 | 25 |
| 8 | 13 |
| 9 | 4 |
| 10 | 3 |

*(Enter your answer as a decimal)*

**Answer:** $6.5$

<details>
<summary>Show Explanation</summary>

### Solution

Add an $fx$ column and find $\sum fx$ and $\sum f$:

$$\sum fx = 3(2)+4(5)+5(10)+6(36)+7(25)+8(13)+9(4)+10(3)$$
$$= 6+20+50+216+175+104+36+30 = 637$$

$$\sum f = 98$$

$$\bar{x} = \frac{\sum fx}{\sum f} = \frac{637}{98} = 6.5$$

</details>

---

## Question 4

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

For the Sydney temperature data:

$$22,\ 23,\ 24,\ 24,\ 26,\ 26,\ 26,\ 27,\ 27,\ 28,\ 28,\ 31,\ 32,\ 34$$

What is the **mode**?

**Options:**
- A) $24$°C
- B) $27$°C
- C) $28$°C
- D) $26$°C

<details>
<summary>Show Explanation</summary>
**Correct Answer: D) $26$°C**


### Solution

The mode is the value that occurs most often. Counting each:
- 26 appears **3 times** (the most frequent)
- 24, 27, 28 each appear 2 times

$$\text{Mode} = 26 \text{°C}$$

</details>

---

## Question 5

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

**True or False:** When a data set contains outliers, the **mean** is the best measure of centre to use.

**Options:**
- A) True
- B) False

<details>
<summary>Show Explanation</summary>
**Correct Answer: B) False**


### Solution

The statement is **False**. When a data set contains outliers (extreme values), the **mean** is pulled towards those extreme values and no longer accurately represents the centre.

In this case, the **median** is the better measure of centre, because it is not affected by outliers — it only depends on the middle value(s), not the extremes.

> **Example:** Salaries of $70K, $78K, $80K, $90K, $180K — the outlier $180K inflates the mean, but the median ($80K) better represents the typical salary.

</details>

---

## Question 6

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

Cameron played in a golf tournament. His **average score** for 4 rounds was 71. His scores in the first 3 rounds were 72, 66, and 70. What was his score in the **4th round**?

*(Enter a numeric answer)*

**Answer:** $76$

<details>
<summary>Show Explanation</summary>

### Solution

**Step 1** — Find the total score for all 4 rounds:

$$\text{Total} = \text{mean} \times n = 71 \times 4 = 284$$

**Step 2** — Find the sum of the first 3 rounds:

$$72 + 66 + 70 = 208$$

**Step 3** — Subtract to find the 4th round:

$$\text{Round 4} = 284 - 208 = 76$$

</details>

---

## Question 7

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

The dot plot below shows the quiz scores (out of 10) for a group of students. Each dot represents one student.

**Interactive Graph:**
```json:mafs
{
  "type": "cartesian",
  "viewBox": { "x": [3.5, 10.5], "y": [0, 6] },
  "preserveAspectRatio": true,
  "elements": [
    { "type": "point", "coordinates": [5, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [6, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [6, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [7, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [7, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [7, 3], "color": "#3b82f6" },
    { "type": "point", "coordinates": [7, 4], "color": "#3b82f6" },
    { "type": "point", "coordinates": [8, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [8, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [9, 1], "color": "#3b82f6" }
  ]
}
```

What is the **median** score?

**Options:**
- A) $7.5$
- B) $7$
- C) $6.5$
- D) $8$

<details>
<summary>Show Explanation</summary>
**Correct Answer: B) $7$**


### Solution

Reading the dot plot, the data values in order are:

$$5,\ 6,\ 6,\ 7,\ 7,\ 7,\ 7,\ 8,\ 8,\ 9$$

There are 10 values (even), so the median is the average of the **5th and 6th values**:

- 5th value: $7$
- 6th value: $7$

$$\text{Median} = \frac{7+7}{2} = 7$$

</details>

---

## Question 8

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

This stem-and-leaf plot shows the pulse rates (beats per minute) of 30 people:

| Stem | Leaf |
|:----:|:-----|
| 5 | 1  5  8 |
| 6 | 1  3  4  4  5  6  8  8  9 |
| 7 | 0  1  2  3  3  4  4  5  7  8  8  9 |
| 8 | 0  3  4  6  7 |
| 9 | 0 |

What is the **median** pulse rate?

**Options:**
- A) $73$
- B) $71$
- C) $72.5$
- D) $74$

<details>
<summary>Show Explanation</summary>
**Correct Answer: C) $72.5$**


### Solution

There are 30 values, so the median is the average of the **15th and 16th values** (counting left to right, top to bottom):

- Stem 5: values 51, 55, 58 → positions 1–3
- Stem 6: 9 values → positions 4–12
- Stem 7: starts at position 13
  - 70 → 13th, 71 → 14th, **72 → 15th**, **73 → 16th**

$$\text{Median} = \frac{72 + 73}{2} = 72.5$$

</details>

---

## Question 9

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

**True or False:** In a stem-and-leaf plot, the **stem** represents the tens digit and the **leaf** represents the units digit (for two-digit numbers).

**Options:**
- A) True
- B) False

<details>
<summary>Show Explanation</summary>
**Correct Answer: A) True**


### Solution

The statement is **True**.

For a two-digit number like 73, the **stem** is the tens digit (7) and the **leaf** is the units digit (3). This allows the full original values to be read from the plot.

For example, in the pulse rate plot:
- Stem 7, Leaf 3 → represents the value **73**
- Stem 8, Leaf 6 → represents the value **86**

</details>

---

## Question 10

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

Two battery brands — **Buzz** and **Eternal** — were tested until failure. Their battery lives (in hours) were recorded in a back-to-back stem-and-leaf plot:

| Buzz (read right→left) | Stem | Eternal (read left→right) |
|:----------------------:|:----:|:-------------------------:|
| 9  8  8 | 0 | |
| 9  8  8  5  2  1  1 | 1 | 4  6  9 |
| 6  3  2  0 | 2 | 4  4  6  8 |
| 1  0 | 3 | 0  1  2  2  5  5  6  7 |

Which battery brand has the **higher median** battery life?

**Options:**
- A) Buzz (median = 18 hours)
- B) They are equal
- C) Eternal (median = 30 hours)
- D) Cannot be determined

<details>
<summary>Show Explanation</summary>
**Correct Answer: C) Eternal (median = 30 hours)**


### Solution

**Buzz** has **16 values**, so the median is the average of the **8th and 9th values**. **Eternal** has **15 values**, so the median is the **8th value**:

**Buzz** (reading right to left, top to bottom): 8, 8, 9, 11, 11, 12, 15, **18**, **18**, 19, 20, 22, 23, 26, 30, 31
$$\text{Median}_{\text{Buzz}} = \frac{18 + 18}{2} = 18 \text{ hours}$$

**Eternal** (reading left to right, top to bottom): 14, 16, 19, 24, 24, 26, 28, **30**, 31, 32, 32, 35, 35, 36, 37
$$\text{Median}_{\text{Eternal}} = 30 \text{ hours}$$

Eternal has the higher median. It is the better-performing battery.

</details>

---

## Question 11

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

A distribution has most of its data values bunched at the **lower end**, with a long tail pointing to the **right**. How is this distribution described?

**Options:**
- A) Negatively skewed
- B) Symmetrical
- C) Positively skewed
- D) Uniform

<details>
<summary>Show Explanation</summary>
**Correct Answer: C) Positively skewed**


### Solution

A **positively skewed** distribution has:
- Most values clustered at the **lower end** (left)
- A **tail pointing to the right** (towards higher values)

A **negatively skewed** distribution is the opposite — clustered at the higher end with a tail pointing **left**.

A **symmetrical** distribution is balanced on both sides of the centre.

</details>

---

## Question 12

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

For a perfectly **symmetrical** distribution, which of the following is true?

**Options:**
- A) The mean is greater than the median
- B) The median is greater than the mode
- C) The mean, median and mode are all equal
- D) The mean is less than the median

<details>
<summary>Show Explanation</summary>
**Correct Answer: C) The mean, median and mode are all equal**


### Solution

For a **symmetrical distribution**, the data is evenly balanced about the centre. This means:

$$\text{mean} = \text{median} = \text{mode}$$

All three measures of centre coincide at the peak of the distribution.

In a **skewed distribution**, the mean is pulled towards the tail, so: mean ≠ median ≠ mode.

</details>

---

## Question 13

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

**True or False:** In a **negatively skewed** distribution, the tail of the graph points to the **left**.

**Options:**
- A) True
- B) False

<details>
<summary>Show Explanation</summary>
**Correct Answer: A) True**


### Solution

The statement is **True**.

A **negatively skewed** distribution has:
- Most data values clustered at the **higher end** (right)
- A **tail that extends to the left** (towards lower values)

Memory tip: the "negative" direction is to the left (negative numbers), so the tail points that way.

In a negatively skewed distribution: $\text{mean} < \text{median} < \text{mode}$

</details>

---

## Question 14

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

The dot plot below shows the scores of a group of students on a test. Each dot represents one student.

**Interactive Graph:**
```json:mafs
{
  "type": "cartesian",
  "viewBox": { "x": [0.5, 11.5], "y": [0, 6] },
  "preserveAspectRatio": true,
  "elements": [
    { "type": "point", "coordinates": [2, 1], "color": "#ef4444" },
    { "type": "point", "coordinates": [6, 1], "color": "#ef4444" },
    { "type": "point", "coordinates": [7, 1], "color": "#ef4444" },
    { "type": "point", "coordinates": [7, 2], "color": "#ef4444" },
    { "type": "point", "coordinates": [8, 1], "color": "#ef4444" },
    { "type": "point", "coordinates": [8, 2], "color": "#ef4444" },
    { "type": "point", "coordinates": [8, 3], "color": "#ef4444" },
    { "type": "point", "coordinates": [9, 1], "color": "#ef4444" },
    { "type": "point", "coordinates": [9, 2], "color": "#ef4444" },
    { "type": "point", "coordinates": [9, 3], "color": "#ef4444" },
    { "type": "point", "coordinates": [9, 4], "color": "#ef4444" },
    { "type": "point", "coordinates": [10, 1], "color": "#ef4444" }
  ]
}
```

How would you describe the **shape** of this distribution?

**Options:**
- A) Positively skewed
- B) Symmetrical
- C) Uniform
- D) Negatively skewed

<details>
<summary>Show Explanation</summary>
**Correct Answer: D) Negatively skewed**


### Solution

Reading the dot plot: most data is **clustered at the high end** (scores 8–10), with a **tail extending to the left** towards lower values (score of 2 is isolated).

This is a **negatively skewed** distribution — the tail points to the **left** (negative direction).

The single dot at score 2 is also likely an **outlier**.

</details>

---

## Question 15

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

A Year 9 Health exam back-to-back stem-and-leaf plot showed:
- Girls' mean: approximately **70.3**
- Boys' mean: approximately **55.8**
- Girls' median: **75**
- Boys' median: **54.5**

Based on these statistics, which group performed **better**?

**Options:**
- A) Boys, because their median is closer to the mean
- B) Girls, because both their mean and median are higher
- C) They performed equally well
- D) Boys, because their data is more spread out

<details>
<summary>Show Explanation</summary>
**Correct Answer: B) Girls, because both their mean and median are higher**


### Solution

Comparing the statistics:

| Statistic | Girls | Boys |
|-----------|-------|------|
| Mean | 70.3 | 55.8 |
| Median | 75 | 54.5 |

The **girls performed better**:
- Their mean (70.3) is significantly higher than the boys' mean (55.8)
- Their median (75) is also higher than the boys' median (54.5)

Both the mean and median consistently show the girls scoring higher, so this conclusion is reliable.

</details>

---

## Question 16

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

A company reports the following salaries for its 10 employees:

$$\$70\,000,\quad \$72\,000,\quad \$78\,500,\quad \$80\,000,\quad \$90\,000,\quad \$93\,000,\quad \$93\,000,\quad \$101\,000,\quad \$105\,000,\quad \$180\,000$$

Which measure of centre **best represents** the typical salary?

**Options:**
- A) Mean, because it uses all the data values
- B) Mode, because it is the most common salary
- C) Median, because it is not affected by the outlier
- D) Range, because it shows the spread

<details>
<summary>Show Explanation</summary>
**Correct Answer: C) Median, because it is not affected by the outlier**


### Solution

The salary $180\,000 is an **outlier** — it is much higher than the others.

- **Mean** = $\frac{\text{sum of all salaries}}{10}$ = $\$96\,250$ — this is inflated by the outlier
- **Median** = average of 5th and 6th values = $\frac{90\,000 + 93\,000}{2} = \$91\,500$ — this is not affected by the outlier

The **median** is the better measure of centre here because it represents the middle of the data without being distorted by the extreme value of $\$180\,000$.

</details>

---

## Question 17

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

**True or False:** The **range** of a data set is affected by outliers.

**Options:**
- A) True
- B) False

<details>
<summary>Show Explanation</summary>
**Correct Answer: A) True**


### Solution

The statement is **True**.

$$\text{Range} = \text{highest value} - \text{lowest value}$$

Because the range uses only the two extreme values, any outlier (which is by definition an extreme value) will directly affect the range, making it appear much larger than the spread of the majority of the data.

**Example:** Data set $\{5, 6, 6, 7, 7, 7, 8\}$ has range $= 3$.
If an outlier is added: $\{1, 5, 6, 6, 7, 7, 7, 8\}$, range $= 7$.

The median and mode are not affected by outliers.

</details>

---

## Question 18

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

How would you classify the data type: **"School report grades (A, B, C, D, E)"**?

**Options:**
- A) Discrete numerical data
- B) Continuous numerical data
- C) Nominal categorical data
- D) Ordinal categorical data

<details>
<summary>Show Explanation</summary>
**Correct Answer: D) Ordinal categorical data**


### Solution

School report grades are **ordinal categorical data**:
- **Categorical** — they are words/symbols, not numbers
- **Ordinal** — they can be placed in a meaningful order (A > B > C > D > E)

Compare with **nominal** data (e.g., hair colour) which cannot be meaningfully ordered.

**Memory tip:** Ordinal → Order. If the categories have a natural ranking, the data is ordinal.

</details>

---

## Question 19

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

How would you classify: **"The temperature in Perth recorded every hour over 24 hours"**?

**Options:**
- A) Discrete numerical data
- B) Ordinal categorical data
- C) Continuous numerical data
- D) Nominal categorical data

<details>
<summary>Show Explanation</summary>
**Correct Answer: C) Continuous numerical data**


### Solution

Temperature is **continuous numerical data**:
- **Numerical** — it is measured as a number
- **Continuous** — temperature can take any value on a smooth scale with no gaps (e.g., 28°C, 28.5°C, 28.73°C, etc.)

Compare with **discrete** numerical data (e.g., number of students) which can only take specific whole number values with "gaps" between them.

</details>

---

## Question 20

**Topic:** Statistics • **Difficulty:** Medium • **Points:** 10

A shoe company wants to test the **durability** of a new running shoe by wearing them until they fall apart. Should the company use a **census** or a **sample**?

**Options:**
- A) Census, because they need results from all shoes
- B) Sample, because testing destroys the shoes
- C) Census, because a sample would be too small
- D) Sample, because the population is too large to identify

<details>
<summary>Show Explanation</summary>
**Correct Answer: B) Sample, because testing destroys the shoes**


### Solution

A **sample** should be used here.

**Reason:** The testing process is **destructive** — each shoe is worn until it fails, making it unusable afterwards. It is impossible to test every single shoe (a census) because there would be no shoes left to sell.

In general, a **sample** is used when:
- Testing would destroy the item
- The population is too large or too expensive to survey entirely
- A representative sample is sufficient for the conclusions needed

A **census** is used when the entire population must be measured (e.g., counting the number of students in a school).

</details>

---
