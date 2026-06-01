---
description: Therap Machine Learning Engineer interview questions, Therap Software Engineer interview details, Therap Machine Learning Engineer interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/therap/ml
---
# Therap Machine Learning Engineer

## Software Engineering Questions

> all code related answers can be answered in any language but python is preferred

<article>

Given an integer N, find all the divisors of N.

<details><summary>Theory and explanation</summary>

A **divisor** (or factor) of a positive integer `N` is any positive integer `d` such that `N % d === 0`.

**Brute force (complete list)**

Iterate `d` from `1` to `N` and collect every `d` that divides `N`. Time **O(N)**, space **O(k)** for `k` divisors.

**Optimized approach (pair enumeration)**

Divisors come in pairs `(d, N/d)`. Scan `d` from `1` to `⌊√N⌋`:

- If `N % d === 0`, both `d` and `N/d` are divisors.
- When `d === N/d` (perfect square), add `d` once.

Sort the result if ascending order is required. Time **O(√N)**, space **O(k)**.

**Interview talking points**

- Clarify whether `N` can be `0` or negative — typically assume **N ≥ 1**.
- Mention that divisor count and sum have number-theoretic formulas, but listing needs enumeration.
- For very large `N`, √N iteration is standard; trial division up to √N also underpins prime testing.

#### Further reading

- [GeeksforGeeks: Find all divisors of a natural number](https://www.geeksforgeeks.org/find-all-divisors-of-a-natural-number-set-2/) — √N pair method
- [MDN: Remainder operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Remainder) — divisibility checks
- [Python: math.isqrt](https://docs.python.org/3/library/math.html#math.isqrt) — integer square root for loop bounds

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function findDivisors(n) {
  if (!Number.isInteger(n) || n <= 0) {
    throw new RangeError('n must be a positive integer');
  }

  const divisors = [];
  for (let d = 1; d * d <= n; d++) {
    if (n % d === 0) {
      divisors.push(d);
      if (d !== n / d) divisors.push(n / d);
    }
  }
  return divisors.sort((a, b) => a - b);
}

findDivisors(12); // [1, 2, 3, 4, 6, 12]
```

#### Code walkthrough

1. Validate `n` is a positive integer.
2. Loop `d` while `d * d ≤ n` to avoid floating-point `sqrt`.
3. On exact division, push the small divisor `d` and its pair `n / d` (unless they are equal).
4. Sort ascending before returning.

#### Complexity

| | |
|-|-|
| Time | O(√N) to scan; O(k log k) if sorting k divisors |
| Space | O(k) for the output list |

#### Edge cases

- **`N = 1`** — only divisor is `[1]`.
- **Perfect squares** — e.g. `N = 36`, `d = 6` must not be duplicated.
- **Large N** — use integer arithmetic; avoid `Math.sqrt` for very large integers in JS (precision limits above `2^53`).

</details>

<details><summary>Solution (other languages)</summary>

```python
import math

def find_divisors(n: int) -> list[int]:
    if n <= 0:
        raise ValueError("n must be positive")
    divisors = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            divisors.append(d)
            if d != n // d:
                divisors.append(n // d)
    return sorted(divisors)

print(find_divisors(12))  # [1, 2, 3, 4, 6, 12]
```

</details>

</article>

<article>

Given two sorted arrays A and B, combine all the elements of A and B into a new sorted array C.

<details><summary>Theory and explanation</summary>

Because **both inputs are already sorted**, merging into a sorted output array is a classic **two-pointer** problem — the same merge step used in merge sort.

**Algorithm**

1. Initialize pointers `i = 0` (A), `j = 0` (B), and empty array `C`.
2. While both pointers are in range, append the smaller of `A[i]` and `B[j]` and advance that pointer.
3. Append any remaining tail from A or B.

This preserves **stability** if you consistently take from A when values are equal (clarify with interviewer).

**Alternatives**

- **Concatenate + sort**: O((m+n) log(m+n)) — simpler but wasteful when inputs are sorted.
- **In-place merge** (if one array has spare capacity at the end): merge from the back — useful in variants like "Merge Sorted Array" on LeetCode.

**Interview talking points**

- State sizes `m = |A|`, `n = |B|`; output length is `m + n`.
- Works for ascending order; for descending, compare with reversed logic or sort after merge.
- Mention this is O(m+n) time, optimal because every element must be read at least once.

#### Further reading

- [LeetCode 88: Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) — in-place variant
- [LeetCode 21: Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) — linked-list version of the same idea
- [Visualgo: Merge Sort](https://visualgo.net/en/sorting) — see the merge step animation

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function mergeSorted(A, B) {
  const C = [];
  let i = 0;
  let j = 0;

  while (i < A.length && j < B.length) {
    if (A[i] <= B[j]) {
      C.push(A[i++]);
    } else {
      C.push(B[j++]);
    }
  }

  while (i < A.length) C.push(A[i++]);
  while (j < B.length) C.push(B[j++]);

  return C;
}

mergeSorted([1, 3, 5], [2, 4, 6]); // [1, 2, 3, 4, 5, 6]
```

#### Code walkthrough

1. Compare front elements of A and B; push the smaller and move that pointer.
2. When one array is exhausted, drain the other with tail loops.
3. Return new array `C` without mutating inputs.

#### Complexity

| | |
|-|-|
| Time | O(m + n) |
| Space | O(m + n) for output (O(1) extra besides output) |

#### Edge cases

- **One array empty** — result is the other array.
- **Duplicates** — both copies appear in output (e.g. `[1,1]` + `[1]` → `[1,1,1]`).
- **Equal elements** — tie-break policy affects stability; `<=` favors A first.

</details>

<details><summary>Solution (other languages)</summary>

```python
def merge_sorted(a: list, b: list) -> list:
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    c.extend(a[i:])
    c.extend(b[j:])
    return c

print(merge_sorted([1, 3, 5], [2, 4, 6]))
```

</details>

</article>

<article>

For a binary tree, you are given a table of two columns N and P, where N represents the id of a node in the tree and P represents the parent of that node in the tree. Write a SQL query to find which the `leaf`, `root` and `inner` nodes and output a table fo the following format

| N         | NodeType                                      |
|----------------|--------------------------------------------------|
| 5 | root |
| 2   | inner |
| 3   | leaf |
| 4   | leaf |
| 8   | inner |
| 6   | leaf |

<details><summary>Theory and explanation</summary>

The table encodes an **adjacency list** for a tree: each row is `(child_id, parent_id)`.

**Node type definitions**

| Type | Condition |
|------|-----------|
| **root** | Node appears as `N` but **never** as anyone's parent `P` in the table — equivalently, the node whose `P IS NULL` (if root row is stored that way), or the unique node not listed in `P` column |
| **leaf** | Node appears as `N` but **never** as a parent `P` — it has no children |
| **inner** | Node is both a child (in `N`) and a parent (in `P`) — has at least one child and is not the root |

**SQL strategy**

1. Build set of all nodes: `N` values union parents in `P` (excluding NULL).
2. **Root**: `N` where `P IS NULL`, or `N NOT IN (SELECT P FROM tree WHERE P IS NOT NULL)`.
3. **Leaf**: `N NOT IN (SELECT DISTINCT P FROM tree WHERE P IS NOT NULL)`.
4. **Inner**: everything else that is in `N`.

Use `CASE` to label types. Order by `N` if required.

**Interview talking points**

- Confirm whether root row uses `P = NULL` or is implied — adjust root detection accordingly.
- Forest vs single tree: multiple roots possible if data is malformed.
- Index on `P` helps joins at scale.

#### Further reading

- [LeetCode 608: Tree Node](https://leetcode.com/problems/tree-node/) — identical classification problem
- [SQLBolt: CASE](https://sqlbolt.com/lesson/conditional) — conditional expressions in SQL
- [PostgreSQL: WITH RECURSIVE](https://www.postgresql.org/docs/current/queries-with.html) — if follow-up asks for depth or paths

</details>

<details><summary>Solution (JavaScript)</summary>

```sql
-- Table: tree(N, P) — N = node id, P = parent id (NULL for root)

SELECT
  N,
  CASE
    WHEN P IS NULL THEN 'root'
    WHEN N NOT IN (SELECT P FROM tree WHERE P IS NOT NULL) THEN 'leaf'
    ELSE 'inner'
  END AS NodeType
FROM tree
ORDER BY N;
```

**Alternative** (when root is the only node not appearing as `P`):

```sql
SELECT
  t.N,
  CASE
    WHEN t.N NOT IN (SELECT P FROM tree WHERE P IS NOT NULL) THEN 'root'
    WHEN t.N NOT IN (SELECT DISTINCT P FROM tree WHERE P IS NOT NULL) THEN 'leaf'
    ELSE 'inner'
  END AS NodeType
FROM tree t
ORDER BY t.N;
```

#### Code walkthrough

1. **`P IS NULL`** identifies the explicit root row (node 5 in the sample).
2. **Leaf test**: node id never appears in the parent column — nodes 3, 4, 6 have no children.
3. **Inner**: nodes that are neither root nor leaf — 2 and 8 have children.
4. `ORDER BY N` matches expected output ordering.

#### Complexity

| | |
|-|-|
| Time | O(n²) with naive `NOT IN` subqueries on n rows; O(n) with joins/hash sets at scale |
| Space | O(n) for subquery materialization |

#### Edge cases

- **Single-node tree** — only root, no leaves in the inner sense (root is also leaf if no children — clarify definition; LeetCode treats root separately via `P IS NULL`).
- **Duplicate rows** — deduplicate with `DISTINCT` if input is messy.
- **Orphan nodes** — nodes whose `P` points to missing parent; flag in data-quality follow-up.

</details>

</article>

## Machine Learning Questions

<article>

You are given realtime 120FPS CCTV footage of cars on a road. Assuming you have a model that can accurately identify cars and output an axis oriented bounding box for every detected car on a single frame. 

You have to detect how many distinct cars that camera has seen in a given timeframe, say within an hour. Given that after a car leaves the camera's field of view, it doesn't appear again. 

Describe how you would approach this problem.

<details><summary>Theory and explanation</summary>

This is a **multi-object tracking (MOT)** and **re-identification across time** problem at high frame rate. The constraint "a car never re-enters" simplifies **global ID assignment**: each new track that persists and exits counts as one distinct vehicle — you do not need long-term re-ID across reappearances.

**Pipeline overview**

1. **Per-frame detection** — Run the provided detector at 120 FPS (or subsample if GPU-bound; see below).
2. **Within-frame association** — NMS on boxes; optional clustering if duplicate boxes per car.
3. **Temporal tracking** — Link detections across frames into **tracks** using:
   - **IoU / centroid matching** (SORT-style) for smooth motion
   - **Kalman filter** for motion prediction between frames
   - Optionally **DeepSORT** appearance embeddings if occlusions cause ID switches
4. **Track lifecycle** — Birth when a stable detection appears; **confirm** after K consecutive frames to suppress false positives; **terminate** when the track leaves FOV or is lost for M frames.
5. **Count distinct cars** — Increment global counter on **confirmed track termination** (car exited) or at end of window count active + terminated unique track IDs.

**120 FPS considerations**

- Full neural detection at 120 FPS may be expensive — **detect every k-th frame** (e.g. 10–15 FPS) and **propagate boxes** with Kalman filter between detections.
- **Edge deployment**: TensorRT / ONNX on GPU; batch size 1 for latency.
- **Async pipeline**: capture → detect → track → aggregate counts in separate threads with bounded queues.

**Metrics and validation**

- **ID switches** (fewer is better), **MOTA/MOTP** on labeled clips.
- Manual count ground truth for an hour-long video segment.

**Interview talking points**

- Distinguish **online** (real-time count) vs **offline** (batch review).
- Handle **occlusions** (trucks hiding sedans) with appearance features.
- Privacy: blur faces/plates if storing video; aggregate counts only.

#### Further reading

- [SORT: Simple Online and Realtime Tracking (paper)](https://arxiv.org/abs/1602.00763) — baseline IoU + Kalman tracking
- [DeepSORT paper](https://arxiv.org/abs/1703.07402) — appearance metric for occlusions
- [OpenCV: KalmanFilter](https://docs.opencv.org/4.x/dd/d6a/classcv_1_1KalmanFilter.html) — motion model between detections
- [NVIDIA DeepStream SDK](https://developer.nvidia.com/deepstream-sdk) — reference multi-stream video analytics pipeline

</details>

<details><summary>Solution (JavaScript)</summary>

High-level **pseudo-architecture** (production would be Python/C++ on edge GPU):

```js
// Conceptual track manager — not production MOT code
class CarCounter {
  constructor() {
    this.nextId = 1;
    this.activeTracks = new Map(); // trackId -> { box, missedFrames, confirmed }
    this.distinctCount = 0;
  }

  onFrame(detections /* [{x,y,w,h,score}] */) {
    const matched = this.associate(this.activeTracks, detections);
    for (const [trackId, det] of matched.updates) {
      this.activeTracks.get(trackId).box = det;
      this.activeTracks.get(trackId).missedFrames = 0;
    }
    for (const trackId of matched.lost) {
      const t = this.activeTracks.get(trackId);
      t.missedFrames++;
      if (t.confirmed && t.missedFrames > MAX_MISSED) {
        this.distinctCount++;
        this.activeTracks.delete(trackId);
      }
    }
    for (const det of matched.newDets) {
      this.activeTracks.set(this.nextId++, {
        box: det,
        missedFrames: 0,
        confirmed: false,
      });
    }
  }
}
```

#### Code walkthrough

- **`associate`** — match detections to tracks by IoU or predicted Kalman box; unmatched detections spawn tracks; unmatched tracks age out.
- **`confirmed`** — require N consecutive hits before counting (reduces phantom cars from noise).
- **On exit** — when a confirmed track is lost beyond threshold, increment `distinctCount`.

#### Complexity

| | |
|-|-|
| Time | O(D × T) per frame for naive IoU matching (D detections, T active tracks); Hungarian O(n³) for optimal assignment |
| Space | O(T) active tracks |

#### Edge cases

- **Brief false detections** — confirmation threshold prevents counting.
- **Stopped traffic** — tracks stay active; do not terminate until exit or timeout policy defined.
- **Partial occlusion** — IoU drops; appearance embedding or higher `MAX_MISSED` helps.

</details>

</article>

<article>

You need to create a model that classified news articles into three categories, 
- sports
- politics
- entertainment

You have large amount of data but there is no labelled data.
The model has to handle very high throughput of hundreds of articles per second at inference time.

Describe how you would approach this problem.

<details><summary>Theory and explanation</summary>

**Constraints:** three-class text classification, **no labels**, **high inference QPS** (100+ articles/sec).

**Phase 1 — Obtain weak or pseudo labels (no manual labels)**

1. **Heuristic / keyword rules** on titles and URLs (e.g. `/sports/`, team names) → noisy seed labels.
2. **Zero-shot classification** with a pretrained model (e.g. NLI-based BART-MNLI, or embedding similarity to class prompts: "This article is about sports").
3. **Clustering** — embed articles (Sentence-BERT, E5); k-means with k=3; map clusters to labels via top keywords or small human review sample.
4. **Self-training / pseudo-labeling** — train on high-confidence predictions; iterate.
5. **Active learning** — label only the most uncertain examples to maximize ROI.

**Phase 2 — Model choice for throughput**

- **Distilled small transformer** (DistilBERT, TinyBERT) or **linear classifier on frozen embeddings** for fastest inference.
- **Traditional baseline**: TF-IDF + linear SVM/logistic regression — extremely fast, strong baseline for news.
- **Serving**: batch inference, ONNX Runtime / TensorRT, model server (TorchServe, Triton), horizontal scaling.
- Target **<10 ms per article** on CPU with linear model; GPU batching for transformers.

**Phase 3 — Quality without full labels**

- Evaluate on a **small gold set** (100–500 articles) labeled manually for sanity.
- Monitor **prediction entropy**, class distribution drift, and keyword sanity checks in production.

**Interview talking points**

- Trade-off: zero-shot LLM APIs vs on-prem small model for cost and latency.
- Multilingual news (Bangla/English) — use multilingual embeddings (`paraphrase-multilingual-MiniLM`).
- Class imbalance — sports may dominate; use balanced sampling or class weights.

#### Further reading

- [Hugging Face: Zero-shot classification pipeline](https://huggingface.co/docs/transformers/main/en/main_classes/pipelines#transformers.ZeroShotClassificationPipeline) — label without training data
- [Sentence-BERT paper](https://arxiv.org/abs/1908.10084) — semantic embeddings for clustering
- [DistilBERT paper](https://arxiv.org/abs/1910.01108) — smaller/faster BERT for serving
- [Google: TFX / bulk inference patterns](https://www.tensorflow.org/tfx/guide/bulk_infer) — high-throughput batch design

</details>

<details><summary>Solution (JavaScript)</summary>

```js
// Illustrative: zero-shot style scoring with precomputed class embeddings
// Production: Python + sentence-transformers / ONNX

const CLASS_PROMPTS = {
  sports: 'sports game match league tournament athlete',
  politics: 'election government parliament policy minister',
  entertainment: 'movie music celebrity film concert show',
};

function cosine(a, b) {
  let dot = 0, na = 0, nb = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    na += a[i] * a[i];
    nb += b[i] * b[i];
  }
  return dot / (Math.sqrt(na) * Math.sqrt(nb));
}

function classify(articleEmbedding, classEmbeddings) {
  let best = 'sports';
  let bestScore = -Infinity;
  for (const [label, emb] of Object.entries(classEmbeddings)) {
    const score = cosine(articleEmbedding, emb);
    if (score > bestScore) {
      bestScore = score;
      best = label;
    }
  }
  return { label: best, confidence: bestScore };
}
```

#### Code walkthrough

1. **Embed** each article title+snippet once (batch for throughput).
2. **Compare** to fixed class prompt embeddings (precomputed offline).
3. **Argmax cosine similarity** yields class; threshold low confidence for "unknown" bucket.
4. **Scale** — embedding service handles 100+ req/s; classifier head is cheap dot products.

#### Complexity

| | |
|-|-|
| Time | O(d) per class per article after embedding (d = dimension); 3 classes → O(3d) ≈ O(1) for fixed d |
| Space | O(d) per stored embedding |

#### Edge cases

- **Multi-topic articles** — return top-2 or multi-label if allowed.
- **Very short text** — fall back to URL rules or defer classification.
- **Label noise from pseudo-labels** — periodic human audit on high-traffic slices.

</details>

</article>

<article>

Given model's training and validation accuracy/loss curve, describe what the graph tells about the model and explain your reasoning. Also describe how you can mitigate the issue the model is facing.

<details><summary>Theory and explanation</summary>

Interviewers show a **learning curve** (epochs vs train/val metrics) and expect you to **diagnose bias/variance** and **training dynamics**.

**Common patterns**

| Pattern | Train | Val | Diagnosis |
|---------|-------|-----|-----------|
| **High bias (underfitting)** | High loss, moderate acc | Similar to train | Model too simple; insufficient capacity or training |
| **High variance (overfitting)** | Loss ↓, acc ↑ | Loss ↑ or acc plateaus/drops while train improves | Memorizing training set |
| **Good fit** | Both improve | Val tracks train with small gap | Healthy training |
| **Val better than train** | — | Val acc > train | Dropout/batch norm during train, or small val set noise — mention cautiously |

**Loss vs accuracy**

- Loss can decrease while accuracy stalls (calibration shifts) — discuss both metrics.

**Mitigations by diagnosis**

**Underfitting**

- Increase model capacity (deeper/wider net, more trees).
- Train longer; tune learning rate.
- Better features; reduce excessive regularization.
- Check for bugs (wrong labels, broken augmentation).

**Overfitting**

- **More data** or **data augmentation**.
- **Regularization**: L2 weight decay, dropout, early stopping on val loss.
- **Simpler model**; reduce features.
- **Cross-validation** for reliable val estimate.
- **Label smoothing**, mixup/cutmix (vision).

**Other issues**

- **Val loss spikes** — learning rate too high; use scheduler, gradient clipping.
- **Both flat** — LR too low or vanishing gradients.
- **Train loss NaN** — LR explosion, bad normalization.

**Interview talking points**

- Always name the **specific curve shape** you see before prescribing fixes.
- Mention **early stopping** as the first practical overfitting knob.
- Distinguish **data leakage** (val too good) from regularization effects.

#### Further reading

- [Scikit-learn: Learning curves](https://scikit-learn.org/stable/modules/learning_curve.html) — bias/variance visualization
- [Deep Learning Book: Ch. 5 — ML basics](https://www.deeplearningbook.org/contents/ml.html) — generalization
- [PyTorch: ReduceLROnPlateau](https://pytorch.org/docs/stable/generated/torch.optim.lr_scheduler.ReduceLROnPlateau.html) — LR scheduling on val plateau
- [Google ML Crash Course: Overfitting](https://developers.google.com/machine-learning/crash-course/overfitting/interpretation) — intuitive guide

</details>

<details><summary>Solution (JavaScript)</summary>

Use this **diagnosis checklist** during the interview when shown a graph:

```js
function diagnoseCurve({ trainLoss, valLoss, trainAcc, valAcc, epoch }) {
  const gap = trainAcc[epoch] - valAcc[epoch];
  const valWorse = valLoss[epoch] > valLoss[epoch - 1];
  const trainImproves = trainLoss[epoch] < trainLoss[epoch - 1];

  if (gap > 0.15 && trainImproves && valWorse) {
    return {
      issue: 'overfitting',
      mitigations: [
        'early stopping',
        'dropout / weight decay',
        'more data or augmentation',
        'reduce model size',
      ],
    };
  }
  if (trainAcc[epoch] < 0.6 && valAcc[epoch] < 0.65) {
    return {
      issue: 'underfitting',
      mitigations: [
        'increase capacity',
        'train longer',
        'tune learning rate',
        'richer features',
      ],
    };
  }
  return { issue: 'healthy or inconclusive', mitigations: ['continue monitoring'] };
}
```

#### Code walkthrough

- **`gap`** — large train–val accuracy gap with worsening val loss signals overfitting.
- **Low absolute accuracy** on both splits suggests underfitting.
- Return **actionable mitigations** tied to the diagnosis, not generic advice.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Small validation set** — noisy val curve; use moving average or k-fold.
- **Different preprocessing on val** — artifact looks like overfitting; verify pipeline parity.

</details>

</article>

<article>

Explain in brief any one research paper you read recently about ML. briefly describe it's methodology, findings and show atleast one real world implication of the paper.

<details><summary>Theory and explanation</summary>

This is a **communication and depth** question — interviewers assess whether you read beyond coursework and can summarize research clearly.

**Recommended answer structure (3–4 minutes spoken)**

1. **Paper identification** — full title, authors, venue/year (NeurIPS, ICML, arXiv, etc.).
2. **Problem** — one sentence on what gap the paper addresses.
3. **Methodology** — model architecture, training objective, dataset, baselines compared.
4. **Key findings** — quantitative result (e.g. "+2.1 BLEU", "40% fewer labels needed") and ablation insight.
5. **Real-world implication** — deployment, product, policy, or engineering practice impact.
6. **Critical note** — one limitation you noticed (shows maturity).

**Example skeleton (you should substitute a paper you actually read)**

- **Paper**: "Attention Is All You Need" (Vaswani et al., 2017) — if discussing classics, say so and pick a recent follow-up (e.g. FlashAttention, LoRA fine-tuning paper).
- **Method**: Self-attention replaces recurrence; positional encoding; multi-head attention.
- **Finding**: Faster parallel training vs LSTM; SOTA on WMT translation at the time.
- **Implication**: Foundation for GPT/BERT-era systems; inference cost drove later work on efficient attention (FlashAttention, sliding window).

**Tips for Therap ML role**

- Prefer papers aligned with **production ML** (efficient inference, tracking, weak supervision) if your background matches.
- Bring one **recent** paper (last 1–2 years) plus know one classic.
- Avoid claiming you read a paper you cannot answer follow-ups on.

#### Further reading

- [arXiv.org](https://arxiv.org/list/cs.LG/recent) — recent ML preprints
- [Papers With Code](https://paperswithcode.com/) — implementations and benchmarks
- [Distill.pub](https://distill.pub/) — visual explanations of key ideas
- [How to read a paper (S. Keshav)](https://web.stanford.edu/class/ee384m/Handouts/HowtoReadPaper.pdf) — efficient reading strategy

</details>

<details><summary>Solution (JavaScript)</summary>

**Response outline template** — replace placeholders with your chosen paper:

```js
const paperSummary = {
  citation:
    'Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models", ICLR 2022',
  problem:
    'Full fine-tuning of billion-parameter models is GPU-heavy and storage-heavy per task.',
  methodology:
    'Freeze pretrained weights; inject trainable low-rank matrices A,B into attention layers so delta-W = BA; train only ~0.1% of parameters.',
  findings:
    'Matches full fine-tuning quality on GLUE/SuperGLUE with far fewer trainable params; multiple LoRA adapters can swap at serving time.',
  realWorldImplication:
    'Enables cheap customization of LLMs in products (support bots, clinical note helpers) on consumer-grade GPUs; Hugging Face PEFT library adoption in industry.',
  limitation:
    'Rank hyperparameter r trades quality vs size; not always optimal for every layer/task.',
};
```

#### Code walkthrough

- Fill each field with **specific numbers and names** from the paper you present.
- **Real-world implication** must be concrete — a product, library, cost saving, or regulation — not "AI will change the world."

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Follow-up**: "How would you reproduce?" — mention dataset, compute, and open-source code availability.
- **Follow-up**: "What's wrong with the evaluation?" — discuss benchmark leakage or narrow tasks.

</details>

</article>
