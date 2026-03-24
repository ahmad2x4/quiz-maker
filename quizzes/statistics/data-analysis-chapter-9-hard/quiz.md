---
id: data-analysis-chapter-9-hard-001
title: "Data Analysis Chapter 9: Hard Questions"
topic: statistics
difficulty: hard
questionCount: 20
createdFrom: "Chapter 9 Data Analysis.pdf"
dateGenerated: "2026-03-23"
estimatedTime: 45
tags: ["mean", "median", "mode", "range", "stem-and-leaf", "dot-plot", "histogram", "distribution", "skew", "outliers", "sampling", "stratified-sample", "comparing-data"]
description: "Challenging Year 9 Data Analysis questions covering measures of centre and spread, distribution shapes, comparing data sets, and sampling methods."
---

# Data Analysis Chapter 9: Hard Questions

## Question 1

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

Tasnuba has completed 5 maths tests. Her mean score is 74. After her 6th test, her mean score increases to 77. What did she score on her 6th test?

*(Enter a numeric answer)*

**Answer:** $92$

<details>
<summary>Show Explanation</summary>

**Correct Answer: $92$**

### Solution

**Step 1** — Find the total of the first 5 tests:

$$\text{Total}_5 = 5 \times 74 = 370$$

**Step 2** — Find the total needed after 6 tests for a mean of 77:

$$\text{Total}_6 = 6 \times 77 = 462$$

**Step 3** — The 6th test score is the difference:

$$\text{Score}_6 = 462 - 370 = 92$$

</details>

---

## Question 2

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

A dataset of 8 values has a mean of 7. What value must be added as a 9th data point so that the new mean becomes 8?

**Options:**
- A) $8$
- B) $15$
- C) $16$
- D) $63$

<details>
<summary>Show Explanation</summary>

**Correct Answer: C) $16$**

### Solution

**Step 1** — Find the current total:

$$\text{Total}_8 = 8 \times 7 = 56$$

**Step 2** — Find the required total after adding the 9th value for a mean of 8:

$$\text{Total}_9 = 9 \times 8 = 72$$

**Step 3** — The 9th value must be:

$$72 - 56 = 16$$

</details>

---

## Question 3

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

Alice has completed 4 maths exams with scores of 64%, 71%, 68%, and 73%. She has one exam left. What score would she need on the 5th exam to achieve a mean of exactly 75%?

**Options:**
- A) $99\%$
- B) $100\%$
- C) $103\%$
- D) It is impossible to achieve a mean of 75%

<details>
<summary>Show Explanation</summary>

**Correct Answer: A) $99\%$**

### Solution

**Step 1** — Total needed for a mean of 75% over 5 exams:

$$5 \times 75 = 375$$

**Step 2** — Current total of the first 4 exams:

$$64 + 71 + 68 + 73 = 276$$

**Step 3** — Required 5th exam score:

$$375 - 276 = 99\%$$

**Verify:** $(276 + 99)/5 = 375/5 = 75\%$ ✓

Alice needs **99%** on her final exam. The challenge here is accurately adding the four scores — a common error is to missum them and get a higher required score.

</details>

---

## Question 4

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

**True or False:** If every value in a dataset is multiplied by 2, then both the mean and the median are also doubled.

**Options:**
- A) True
- B) False

<details>
<summary>Show Explanation</summary>

**Correct Answer: A) True**

### Solution

**Mean:** If the original mean is $\bar{x} = \dfrac{\sum x_i}{n}$, then after multiplying every value by 2:

$$\bar{x}_{\text{new}} = \frac{\sum 2x_i}{n} = 2 \cdot \frac{\sum x_i}{n} = 2\bar{x}$$

**Median:** The median is the middle value (or average of the two middle values) when data is ordered. If every value is doubled, the order stays the same and the middle value(s) are also doubled:

$$\text{Median}_{\text{new}} = 2 \times \text{Median}_{\text{original}}$$

Both the mean and median are doubled. The statement is **True**.

</details>

---

## Question 5

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

A company's annual salaries (in dollars) are: 48 000, 52 000, 55 000, 58 000, 61 000, 65 000, 180 000. Which measure is affected the **most** when the $180 000 salary is added to an otherwise complete dataset of the remaining six values?

**Options:**
- A) Mean
- B) Median
- C) Mode
- D) Range

<details>
<summary>Show Explanation</summary>

**Correct Answer: D) Range**

### Solution

Without $180 000$, consider the six salaries: 48 000, 52 000, 55 000, 58 000, 61 000, 65 000.

- **Range** without outlier: $65\,000 - 48\,000 = 17\,000$
- **Range** with outlier: $180\,000 - 48\,000 = 132\,000$ — increases by $115\,000$ (a factor of ~7.8×)

- **Mean** without outlier: $(48\,000 + 52\,000 + 55\,000 + 58\,000 + 61\,000 + 65\,000)/6 = 339\,000/6 = 56\,500$
- **Mean** with outlier: $519\,000/7 \approx 74\,143$ — increases by ~$17\,643$

The range changes by a far greater proportion than the mean. The **range** is the most affected measure.

Note: The mode is unchanged (there is no mode in this dataset). The median shifts only slightly.

</details>

---

## Question 6

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

A class records quiz scores. The cumulative frequency table is shown below.

| Score | Frequency | Cumulative Frequency |
|-------|-----------|----------------------|
| 4     | 3         | 3                    |
| 5     | 8         | 11                   |
| 6     | 18        | 29                   |
| 7     | 24        | 53                   |
| 8     | 15        | 68                   |
| 9     | 7         | 75                   |

What is the **median** score?

**Options:**
- A) $6$
- B) $6.5$
- C) $7$
- D) $7.5$

<details>
<summary>Show Explanation</summary>

**Correct Answer: C) $7$**

### Solution

There are 75 values in total. The median is the $\dfrac{75+1}{2} = 38$th value.

Reading the cumulative frequency column:
- Scores up to 6: cumulative frequency = 29 (the 29th value is a 6)
- Scores up to 7: cumulative frequency = 53 (the 53rd value is a 7)

The 38th value lies between the 30th and 53rd values — all of which have a score of **7**.

$$\text{Median} = 7$$

</details>

---

## Question 7

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

A stem-and-leaf plot shows the pulse rates (beats per minute) of 30 students:

| Stem | Leaves            |
|------|-------------------|
| 5    | 0 0 1 5           |
| 6    | 0 2 3 5 6 8 9     |
| 7    | 0 1 2 2 3 4 5 6 7 8 9 |
| 8    | 0 1 2 3 5 8       |
| 9    | 0 2               |

What is the **mean** pulse rate? Round your answer to one decimal place.

**Options:**
- A) $71.9$
- B) $72.5$
- C) $73.0$
- D) $70.8$

<details>
<summary>Show Explanation</summary>

**Correct Answer: A) $71.9$**

### Solution

List all values and compute the sum:

| Stem | Values | Sum |
|------|--------|-----|
| 5    | 50, 50, 51, 55 | 206 |
| 6    | 60, 62, 63, 65, 66, 68, 69 | 453 |
| 7    | 70, 71, 72, 72, 73, 74, 75, 76, 77, 78, 79 | 817 |
| 8    | 80, 81, 82, 83, 85, 88 | 499 |
| 9    | 90, 92 | 182 |

$$\text{Total} = 206 + 453 + 817 + 499 + 182 = 2157$$

$$n = 4 + 7 + 11 + 6 + 2 = 30$$

$$\text{Mean} = \frac{2157}{30} = 71.9 \text{ bpm}$$

</details>

---

## Question 8

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

Two brands of batteries are tested. The back-to-back stem-and-leaf plot shows their lifetimes (hours):

| Eternal (leaves) | Stem | Buzz (leaves) |
|-----------------|------|---------------|
| 6               | 1    | 0 2 4 6 8 8   |
| 8 8 6 4 2       | 2    | 0 2 4 5       |
| 8 5 2 0         | 3    |               |

*(Eternal leaves are read right-to-left from the stem; Buzz leaves are read left-to-right.)*

The mean lifetime of **Eternal** batteries is $27.9$ hours. What is the **difference** between the mean lifetime of Eternal and the mean lifetime of Buzz batteries (to the nearest whole number)?

**Options:**
- A) $5$ hours
- B) $8$ hours
- C) $10$ hours
- D) $12$ hours

<details>
<summary>Show Explanation</summary>

**Correct Answer: C) $10$ hours**

### Solution

**Eternal battery lifetimes** (reading each row right-to-left from the stem):

$$16,\quad 22, 24, 26, 28, 28,\quad 30, 32, 35, 38$$

$$\text{Mean}_{\text{Eternal}} = \frac{16+22+24+26+28+28+30+32+35+38}{10} = \frac{279}{10} = 27.9 \text{ hours}$$

**Buzz battery lifetimes** (reading each row left-to-right from the stem):

$$10, 12, 14, 16, 18, 18,\quad 20, 22, 24, 25$$

$$\text{Mean}_{\text{Buzz}} = \frac{10+12+14+16+18+18+20+22+24+25}{10} = \frac{179}{10} = 17.9 \text{ hours}$$

**Difference:**

$$27.9 - 17.9 = 10 \text{ hours}$$

</details>

---

## Question 9

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

**True or False:** In the pulse rate stem-and-leaf data from Question 7, there is exactly one mode.

**Options:**
- A) True
- B) False

<details>
<summary>Show Explanation</summary>

**Correct Answer: B) False**

### Solution

The **mode** is the value that appears most frequently. Scanning the stem-and-leaf plot from Question 7:

- **50** appears twice (two leaves of 0 in the 5 stem)
- **72** appears twice (two leaves of 2 in the 7 stem)
- All other values appear exactly once

Both 50 and 72 each appear twice — the maximum frequency. This means the dataset has **two modes** (50 and 72), not exactly one.

The statement is **False**.

</details>

---

## Question 10

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

The dot plot below shows the reaction times (milliseconds) of 10 participants in a study. One participant recorded an unusually high time.

**Interactive Graph:**
```json:mafs
{
  "type": "cartesian",
  "viewBox": { "x": [12, 42], "y": [0, 5] },
  "preserveAspectRatio": true,
  "elements": [
    { "type": "point", "coordinates": [15, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [18, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [19, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [20, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [20, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [21, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [22, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [22, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [23, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [38, 1], "color": "#ef4444" }
  ]
}
```

What is the **median** reaction time?

**Options:**
- A) $20$ ms
- B) $20.5$ ms
- C) $21$ ms
- D) $22$ ms

<details>
<summary>Show Explanation</summary>

**Correct Answer: B) $20.5$ ms**

### Solution

Reading the dot plot, the 10 values in order are:

$$15, 18, 19, 20, 20, 21, 22, 22, 23, 38$$

With 10 values (even number), the median is the average of the 5th and 6th values:

$$\text{Median} = \frac{20 + 21}{2} = \frac{41}{2} = 20.5 \text{ ms}$$

Note: The outlier at 38 ms does not affect the median significantly — this illustrates why median is more robust than mean for skewed data.

</details>

---

## Question 11

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

For a **positively skewed** distribution, which ordering of the three measures of centre is correct?

**Options:**
- A) $\text{mean} < \text{median} < \text{mode}$
- B) $\text{mode} < \text{median} < \text{mean}$
- C) $\text{median} < \text{mode} < \text{mean}$
- D) $\text{mean} = \text{median} = \text{mode}$

<details>
<summary>Show Explanation</summary>

**Correct Answer: B) $\text{mode} < \text{median} < \text{mean}$**

### Solution

In a **positively skewed** (right-skewed) distribution:
- The **tail** extends to the **right** (towards higher values)
- High outliers pull the **mean** upward most strongly
- The **median** is less affected by extreme values
- The **mode** is at the peak of the distribution (the left side, where most data clusters)

This gives the ordering:

$$\text{mode} < \text{median} < \text{mean}$$

A simple memory trick: for positive skew, the mean is "pulled" in the positive (right) direction past the median and mode.

</details>

---

## Question 12

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

**True or False:** For a negatively skewed distribution, the mean is greater than the median.

**Options:**
- A) True
- B) False

<details>
<summary>Show Explanation</summary>

**Correct Answer: B) False**

### Solution

In a **negatively skewed** (left-skewed) distribution:
- The **tail** extends to the **left** (towards lower values)
- Low outliers pull the **mean** downward
- The **median** sits above the mean

The correct ordering for a negatively skewed distribution is:

$$\text{mean} < \text{median} < \text{mode}$$

Therefore, the mean is **less than** the median — the statement is **False**.

</details>

---

## Question 13

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

A frequency histogram for a set of data shows two distinct peaks separated by a valley. What term best describes this distribution shape?

**Options:**
- A) Unimodal
- B) Uniform
- C) Bimodal
- D) Positively skewed

<details>
<summary>Show Explanation</summary>

**Correct Answer: C) Bimodal**

### Solution

A distribution with **two distinct peaks** is called **bimodal** — it has two modes (two values or intervals that are most frequent).

- **Unimodal**: one peak
- **Bimodal**: two peaks
- **Multimodal**: three or more peaks
- **Uniform**: approximately equal frequency across all values (flat shape)
- **Skewed**: one tail is longer than the other

Two peaks separated by a valley is the defining feature of a bimodal distribution.

</details>

---

## Question 14

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

The dot plot below shows the scores of 9 students on a test.

**Interactive Graph:**
```json:mafs
{
  "type": "cartesian",
  "viewBox": { "x": [0, 9], "y": [0, 4] },
  "preserveAspectRatio": true,
  "elements": [
    { "type": "point", "coordinates": [1, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [1, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [2, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [2, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [5, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [6, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [6, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [7, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [7, 2], "color": "#3b82f6" }
  ]
}
```

Which statement best describes the distribution and the relationship between mean and median?

**Options:**
- A) Positively skewed; mean $>$ median
- B) Negatively skewed; mean $<$ median
- C) Bimodal; mean $\approx$ median
- D) Uniform; mean $=$ median

<details>
<summary>Show Explanation</summary>

**Correct Answer: C) Bimodal; mean $\approx$ median**

### Solution

The data values read from the dot plot are: 1, 1, 2, 2, 5, 6, 6, 7, 7.

**Shape:** There are two clusters — one at 1–2 and another at 6–7 — with a gap around 3–4 and a single value at 5. This is a **bimodal** distribution.

**Mean:**
$$\bar{x} = \frac{1+1+2+2+5+6+6+7+7}{9} = \frac{37}{9} \approx 4.1$$

**Median:** The 5th value in the ordered list (1, 1, 2, 2, **5**, 6, 6, 7, 7) is **5**.

The mean ($\approx 4.1$) and median ($= 5$) are both in the middle of the distribution, approximately equal. The distribution is **bimodal** with mean $\approx$ median.

</details>

---

## Question 15

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

A school has two maths classes. Class A (37 students) achieves a mean score of 58. Class B (40 students) achieves a mean score of 67. What is the mean score for all 77 students combined? (Round to one decimal place.)

**Options:**
- A) $62.5$
- B) $62.7$
- C) $63.0$
- D) $63.5$

<details>
<summary>Show Explanation</summary>

**Correct Answer: B) $62.7$**

### Solution

**Step 1** — Find the total score for each class:

$$\text{Total}_A = 37 \times 58 = 2146$$
$$\text{Total}_B = 40 \times 67 = 2680$$

**Step 2** — Find the combined total and number of students:

$$\text{Total combined} = 2146 + 2680 = 4826$$
$$n = 37 + 40 = 77$$

**Step 3** — Calculate the combined mean:

$$\bar{x} = \frac{4826}{77} = 62.675\ldots \approx 62.7$$

Note: You **cannot** simply average the two means ($\frac{58+67}{2} = 62.5$) because the classes have different sizes. A weighted mean must be used.

</details>

---

## Question 16

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

Brooke and Ryan each completed 5 sprint times (seconds). Brooke's times: 10.12, 10.34, 10.28, 10.19, 10.41. Ryan's times: 10.05, 11.22, 10.78, 13.60, 9.05. Who is **more consistent**, and why?

**Options:**
- A) Ryan, because his fastest time is lower
- B) Brooke, because her range is smaller
- C) Ryan, because his mean is lower
- D) Brooke, because her mean is lower

<details>
<summary>Show Explanation</summary>

**Correct Answer: B) Brooke, because her range is smaller**

### Solution

**Consistency** in statistics is measured by **spread** — smaller spread means more consistent.

**Brooke's range:**
$$10.41 - 10.12 = 0.29 \text{ s}$$

**Ryan's range:**
$$13.60 - 9.05 = 4.55 \text{ s}$$

Brooke's times are clustered tightly together (range = 0.29 s), while Ryan's times vary widely (range = 4.55 s).

**Brooke is more consistent** because her range is much smaller — her performance varies little from run to run.

</details>

---

## Question 17

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

**True or False:** From the data in Question 16, Ryan's range is larger than Brooke's range, so Brooke's sprint times are more consistent.

**Options:**
- A) True
- B) False

<details>
<summary>Show Explanation</summary>

**Correct Answer: A) True**

### Solution

- **Brooke's range:** $10.41 - 10.12 = 0.29$ s
- **Ryan's range:** $13.60 - 9.05 = 4.55$ s

Ryan's range ($4.55$ s) is indeed larger than Brooke's range ($0.29$ s).

A **larger range** means **greater variability** — Ryan's times are more spread out. Therefore, **Brooke's times are more consistent** (less variable).

The statement is **True**.

</details>

---

## Question 18

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

A school has 872 students. A stratified sample of 100 students is to be selected by year group. Year 9 has 160 students. How many Year 9 students should be included in the sample?

**Options:**
- A) $16$
- B) $18$
- C) $20$
- D) $22$

<details>
<summary>Show Explanation</summary>

**Correct Answer: B) $18$**

### Solution

In a stratified sample, each group is represented **proportionally**.

$$\text{Year 9 proportion} = \frac{160}{872}$$

$$\text{Year 9 in sample} = \frac{160}{872} \times 100 = \frac{16000}{872} \approx 18.35 \approx 18$$

So approximately **18** Year 9 students should be included.

**Why stratified sampling?** It ensures that every year group is fairly represented — without it, a simple random sample might over- or under-represent certain groups.

</details>

---

## Question 19

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

Using the same school from Question 18 (872 students total, stratified sample of 100), Year 12 has 128 students. How many Year 12 students should be included in the sample?

*(Enter a numeric answer — round to the nearest whole number)*

**Answer:** $15$

<details>
<summary>Show Explanation</summary>

**Correct Answer: $15$**

### Solution

$$\text{Year 12 in sample} = \frac{128}{872} \times 100 = \frac{12800}{872} \approx 14.68 \approx 15$$

**15** Year 12 students should be selected.

Note: $14.68$ rounds to $15$ (not $14$), since the decimal part ($0.68$) is greater than $0.5$.

</details>

---

## Question 20

**Topic:** Statistics • **Difficulty:** Hard • **Points:** 10

The dot plot below shows the number of hours per week that 9 students spend on social media.

**Interactive Graph:**
```json:mafs
{
  "type": "cartesian",
  "viewBox": { "x": [0, 9], "y": [0, 4] },
  "preserveAspectRatio": true,
  "elements": [
    { "type": "point", "coordinates": [1, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [1, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [2, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [2, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [5, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [6, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [6, 2], "color": "#3b82f6" },
    { "type": "point", "coordinates": [7, 1], "color": "#3b82f6" },
    { "type": "point", "coordinates": [7, 2], "color": "#3b82f6" }
  ]
}
```

A student claims: "Because the data has two clusters, the mean is not a useful measure of centre." Is this claim correct?

**Options:**
- A) No — the mean is always the best measure of centre
- B) Yes — for bimodal data, neither cluster is well represented by the mean
- C) No — the mean equals the median here, so it is reliable
- D) Yes — but only because there is an outlier in the data

<details>
<summary>Show Explanation</summary>

**Correct Answer: B) Yes — for bimodal data, neither cluster is well represented by the mean**

### Solution

The data: 1, 1, 2, 2, 5, 6, 6, 7, 7 forms two clusters (1–2 and 6–7).

$$\text{Mean} = \frac{1+1+2+2+5+6+6+7+7}{9} = \frac{37}{9} \approx 4.1$$

The mean of approximately 4.1 falls **between** the two clusters (in the gap around 3–5). No student actually scored near 4.1 — so the mean does not represent the "typical" student in either cluster.

For **bimodal** distributions, the mean falls in the gap between modes and fails to represent the data well. The student's claim is **correct** — the median (5) or reporting both modes (1–2 and 6–7) would give a more informative description.

</details>

---
