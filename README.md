<div align="center">
  <h1>🚀 Data Structures & Algorithms Mastery</h1>
  <p><i>A comprehensive, production-grade repository of 270+ curated DSA solutions, algorithmic patterns, foundational paradigms, and language mastery in Python & Java.</i></p>

  <!-- Badges -->
  <p>
    <a href="https://github.com/Priy4n5hu21072005/DSA/graphs/contributors"><img src="https://img.shields.io/github/contributors/Priy4n5hu21072005/DSA?style=for-the-badge&color=orange" alt="Contributors" /></a>
    <a href="https://github.com/Priy4n5hu21072005/DSA/stargazers"><img src="https://img.shields.io/github/stars/Priy4n5hu21072005/DSA?style=for-the-badge&color=yellow" alt="Stars" /></a>
    <img src="https://img.shields.io/badge/Languages-Python%203%20%7C%20Java-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Languages" />
    <img src="https://img.shields.io/badge/Total%20Files-275-success?style=for-the-badge" alt="Total Files" />
    <img src="https://img.shields.io/badge/Solutions-250%2B%20Problems-blueviolet?style=for-the-badge" alt="Solutions" />
    <img src="https://img.shields.io/badge/Focus-Patterns%20%26%20Optimizations-red?style=for-the-badge" alt="Focus" />
  </p>
</div>

---

## 📖 Table of Contents
1. [About The Repository](#-about-the-repository)
2. [Workspace Statistics](#-workspace-statistics)
3. [Repository Structure Tree](#-repository-structure-tree)
4. [Deep-Dive into Modules](#-deep-dive-into-modules)
    - [1. Algorithms (106 Files)](#1-algorithms-106-files)
    - [2. Data Structures (114 Files)](#2-data-structures-114-files)
        - [Graph 6-Phase Mastery Roadmap](#-graph-6-phase-mastery-roadmap)
    - [3. Daily Contest Solutions (20 Files)](#3-daily-contest-solutions-20-files)
    - [4. Revision & Rapid Recall (5 Files)](#4-revision--rapid-recall-5-files)
    - [5. Java Revision & Practice (13 Files)](#5-java-revision--practice-13-files)
    - [6. Python Fundamentals & OOP (16 Files)](#6-python-fundamentals--oop-16-files)
5. [Boilerplate Templates & Roadmaps](#-boilerplate-templates--roadmaps)
6. [🚀 Getting Started](#-getting-started)
7. [🛠️ Running Solutions](#%EF%B8%8F-running-solutions)
8. [🤝 Contributing](#-contributing)
9. [📄 License](#-license)

---

## 📖 About The Repository

Welcome to the **Data Structures and Algorithms (DSA) Mastery** workspace! This repository is an engineered, systematic environment tailored for excelling in technical interviews, competitive programming (LeetCode, GFG, Contests), and core computer science foundations.

Rather than treating problem-solving as an unstructured list of ad-hoc problems, this codebase groups techniques into **algorithmic patterns** (*Two Pointers*, *Sliding Window*, *Monotonic Stack*, *Priority Queue/Heap*, *State-Space Backtracking*) and **custom data structure implementations** (*Graph BFS/DFS/DSU*, *Binary Trees*, *Queues*, *Linked Lists*, *Stacks*).

### 🌟 Key Highlights
- **Polyglot Repository:** Core problem solutions primarily crafted in high-efficiency **Python 3**, with comprehensive object-oriented and advanced paradigms implemented in **Java**.
- **Pattern-Oriented Architecture:** Problems are categorized by underlying structural logic to promote intuition over memorization.
- **Built-In Roadmaps & Templates:** Contains curated learning roadmaps (e.g. Graph 6-Phase sequence, curated Revision sequence) and standard algorithmic boilerplates (`templet.txt`).
- **Comprehensive OOP Foundations:** Chapter-by-chapter implementations covering encapsulation, polymorphism, inheritance, custom comparators, lambdas, streams, and collection frameworks.

---

## 📊 Workspace Statistics

| Category | Sub-categories / Components | Files | Primary Language |
| :--- | :--- | :---: | :---: |
| **Algorithms** | Backtracking, Binary Search, DFS, Monotonic Stack, Prefix Sum, Heap, Recursion, Sliding Window, Sorting, Two Pointers | `106` | Python |
| **Data Structures** | Array & Sorting, Graph (BFS, DFS, Dijkstra, DSU, TopoSort), LinkedList, Queue, Stack, Binary & Search Tree | `114` | Python |
| **Daily Contest** | LeetCode Biweekly, Weekly & Daily Challenge problems | `20` | Python |
| **Revision** | High-yield interview problems & 20-problem rapid sequence | `5` | Python / Text |
| **Java Revision** | Access Modifiers, Advanced Java (Streams, Comparators), Collections, OOP Concepts, Static/Instance | `13` | Java |
| **Python Fundamentals** | OOP Principles (Ch 1-5), Native Data Structures, Top 10 LeetCode Interview Problems | `16` | Python |
| **Root Documentation** | Comprehensive project documentation and guides | `1` | Markdown |
| **Total** | **Full Workspace Overview** | **`275`** | **Python & Java** |

---

## 📁 Repository Structure Tree

A structural view of the directories and file allocations across the workspace:

```text
DSA/
├── Algorithms/                             # 106 Files - Core Algorithmic Problem-Solving Strategies
│   ├── Backtracking/                       # 14 files (N-Queens, Sudoku, Combinations, Permutations, Template)
│   ├── Binary-Search/                      # 5 files (2D Matrix search, Rotated arrays, Complete trees, LIS)
│   ├── DFS/                                # 4 files (Tree path sums, depth checks, DFS template)
│   ├── Dynamic Programing/                 # (Reserved module for upcoming DP state machines)
│   ├── Monotonic-Stack/                    # 7 files (Next Greater I/II, Daily Temperatures, Subarray Minimums)
│   ├── Prefix-Sum/                         # 9 files (Subarray sum equals K, 2D range sum, Product except self)
│   ├── Priority-Queue(Heap)/               # 17 files (Top K frequent, Median finder, IPO, Merge K lists, Twitter)
│   ├── Recurrsion/                         # 2 files (Ways to add parentheses, Permutation sequences)
│   ├── Sliding-Window/                     # 18 files (Fixed/variable window, Min window substring, Anagrams)
│   ├── Sorting/                            # 10 files (Interval merges, List sorts, Custom orderings, Colors)
│   └── Two-Pointers/                       # 20 files (Trapping rain water, 3Sum, Container with most water)
├── Data-Structures/                        # 114 Files - Data Structures, Implementations & Problem Sets
│   ├── Array/                              # 12 files (Kadane's, Plus One, Equilibrium point + 8 Sorting implementations)
│   ├── GraphDataStructure/                 # 29 files (Fundamentals, Multi-source BFS, Grid BFS, DFS, Dijkstra, DSU, Kahn's)
│   ├── LinkedList/                         # 9 files (Nth node operations, Reverse, Two-pointer scans, Merging)
│   ├── QueueDataStructure/                 # 10 files (List/Deque representations, Circular queue, Rotten oranges)
│   ├── Stack/                              # 15 files (Array stack, MinStack, Polish notation, Parentheses, Decode string)
│   └── Tree/                               # 39 files (Binary trees, Balance trees, BST CRUD, Traversals, Path sums)
├── DailyContest/                           # 20 Files - Recent LeetCode & Competitive Contest Solutions
├── Revision/                               # 5 Files - Rapid Review Solutions & Curated Problem Sequence Roadmap
├── JavaRevisionAndPractice/                # 13 Files - Java Core, OOP Principles, Collections & Advanced APIs
│   ├── AccessModifiers/                    # 1 file (Private, package-private, protected, public encapsulation)
│   ├── AdvanceJava/                        # 5 files (Chapters 1-3, Custom Comparators, Lambda/Streams Driver)
│   ├── CollectionFramework/                # 2 files (ArrayList dynamics, List interface mechanics)
│   ├── OOPSConcepts/                       # 3 files (Chapters 1-3: Inheritance, Polymorphism, Abstraction)
│   └── (Root files)                        # 2 files (Static vs. Instance method execution and memory allocation)
└── PythonFundamentalsAndOOP/               # 16 Files - Python Language Mastery & Top Interview Revision
    ├── OopsConcept/                        # 5 files (Chapters 1-5: Classes, Dunder methods, Inheritance, Encapsulation)
    ├── PythonDataStructure/                # 1 file (Built-in data types, dictionary, list, and set idioms)
    └── RevisionLeetcodeInterviewQuestion/  # 10 files (Two Sum, Stock Buy/Sell, Palindrome, Duplicates, Majority Element)
```

---

## 🔍 Deep-Dive into Modules

### 1. Algorithms (106 Files)

Core algorithmic problem patterns equipped with template scripts and progressive problem implementations:

| Pattern / Category | Files | Key Highlights & LeetCode Problems Solved | Explore |
| :--- | :---: | :--- | :---: |
| **Backtracking** | `14` | Algorithmic template (`templet.txt`), N-Queens (`p51`, `p52`), Sudoku Solver (`p37`), Combination Sum I/II (`p39`, `p40`), Permutations I/II (`p46`, `p47`), Combinations (`p77`), Word Search (`p79`), BST Validation (`p98`, `p99`, `p100`, `p101`). | [📂 Backtracking](./Algorithms/Backtracking/) |
| **Binary Search** | `5` | 2D Matrix Search (`p74`, `p240`), Rotated Sorted Array II (`p81`), Count Complete Tree Nodes (`p222`), Longest Increasing Subsequence with Binary Search (`p300`). | [📂 Binary Search](./Algorithms/Binary-Search/) |
| **DFS** | `4` | DFS template (`templete.txt`), Balanced Tree validation (`p110`), Minimum Depth (`p111`), Path Sum (`p112`). | [📂 DFS](./Algorithms/DFS/) |
| **Monotonic Stack** | `7` | Pattern template (`templete.txt`), Next Greater Element I/II (LC 496, 503), Daily Temperatures (LC 739), Sum of Subarray Minimums (LC 907), Final Prices (LC 1475), Subarray Range Sum (LC 2104). | [📂 Monotonic Stack](./Algorithms/Monotonic-Stack/) |
| **Prefix Sum** | `9` | Subarray Sum Divisible / Continuous (LC 523), Contiguous Array 0/1 (LC 525), Pivot Index (LC 724), Product of Array Except Self (LC 238), Range Sum Query 1D/2D (LC 303, 304), Split Array Largest Sum (LC 410), Random Rectangles (LC 497). | [📂 Prefix Sum](./Algorithms/Prefix-Sum/) |
| **Priority Queue / Heap** | `17` | Merge K Sorted Lists (LC 23), Kth Largest Element (LC 215, 703), Ugly Number II (LC 264), Find Median from Data Stream (LC 295), Top K Frequent Elements & Words (LC 347, 692), Design Twitter (LC 355), K Pairs Smallest Sum (LC 373), Kth Smallest in Matrix (LC 378), Frequency Sort (LC 451), Sliding Window Median (LC 480), IPO (LC 502), Relative Ranks (LC 506), Split Array (LC 659), K Closest Points (LC 973), Last Stone Weight (LC 1046). | [📂 Priority Queue](./Algorithms/Priority-Queue(Heap)/) |
| **Recursion** | `2` | Different Ways to Add Parentheses (LC 241), Permutation Sequence (LC 60). | [📂 Recursion](./Algorithms/Recurrsion/) |
| **Sliding Window** | `18` | Algorithm template (`templete.txt`), Sliding Window Maximum (LC 239), Maximum Subarray Average (LC 643), Permutation in String (LC 567), Longest Harmonious Subsequence (LC 594), K Closest Elements (LC 658), Subarray Product Less Than K (LC 713), Max Length Repeated Subarray (LC 718), Substring with Concatenation (LC 30), Minimum Window Substring (LC 76), Repeated DNA (LC 187), Contains Duplicate II/III (LC 219, 220), Longest Substring with At Least K Repeating (LC 395), Character Replacement (LC 424), All Anagrams (LC 438). | [📂 Sliding Window](./Algorithms/Sliding-Window/) |
| **Sorting** | `10` | Merge Intervals (LC 56), Insertion Sort List (LC 147), Sort List (LC 148), Maximum Gap (LC 164), Majority Element I/II (LC 169, 229), Largest Number (LC 179), Kth Largest Element (LC 215), Move Zeroes (LC 283). | [📂 Sorting](./Algorithms/Sorting/) |
| **Two Pointers** | `20` | Container With Most Water (LC 11), 3Sum (LC 15), Trapping Rain Water (LC 42), Sort Colors / Dutch National Flag (LC 75), Remove Duplicates II (LC 80), Partition List (LC 86), Merge Sorted Array (LC 88), Two Sum II Sorted (LC 167), Rotate Array (LC 189), Happy Number (LC 202), Reverse Vowels (LC 345), Array Intersection I/II (LC 349, 350), Is Subsequence (LC 392), String Compression (LC 443). | [📂 Two Pointers](./Algorithms/Two-Pointers/) |

---

### 2. Data Structures (114 Files)

Custom implementations, core operations, and canonical problem sets across all fundamental data structures:

| Data Structure | Files | Sub-modules & Topic Coverage | Explore |
| :--- | :---: | :--- | :---: |
| **Array & Sorting** | `12` | Kadane's algorithm (`P53`), Plus One (`p66`), GFG Adding One & Equilibrium Point, plus custom sorting implementations: **Bubble Sort**, **Insertion Sort**, **Selection Sort**, **Merge Sort**, and **Quick Sort** with revision variations. | [📂 Array](./Data-Structures/Array/) |
| **Graph Data Structure** | `29` | Adjacency Matrix & List representations, Graph Degree, Simple BFS, Grid BFS, Multi-Source BFS, Connected/Disconnected DFS, Dijkstra Shortest Path, Kahn's Topological Sort (BFS & DFS), Disjoint Set Union (Rank & Size), and extensive BFS/DFS problem sets. | [📂 Graph](./Data-Structures/GraphDataStructure/) |
| **Linked List** | `9` | Singly Linked List operations: Length, Print, Search, Get Nth Node, Get Nth Node from End (standard & Two-Pointer approach), Remove Linked List Elements (LC 203), Reverse Linked List (LC 206), and Merge Two Sorted Lists (LC 21). | [📂 LinkedList](./Data-Structures/LinkedList/) |
| **Queue** | `10` | Implementations via Python `list` and `collections.deque`, Circular Queue (LC 622), Implement Queue using Stacks (LC 232), Recent Counter (LC 933), Reveal Cards (LC 950), Rotting Oranges (LC 994), Students Lunch (LC 1700), Time Needed to Buy Tickets (LC 2073). | [📂 Queue](./Data-Structures/QueueDataStructure/) |
| **Stack** | `15` | Custom Array Stack (`ArrayRepresentationOfStack.py`), Min Stack (LC 155), Evaluate Reverse Polish Notation (LC 150), Decode String (LC 394), Baseball Game (LC 682), Backspace String Compare (LC 844), Remove Adjacent Duplicates (LC 1047), Build Array with Stack Ops (LC 1441), Make String Great (LC 1544), Crawler Log Folder (LC 1598), Valid Parentheses (LC 20), Stack using Queues (LC 225), Next Greater Element I (LC 496), Daily Temperatures (LC 739). | [📂 Stack](./Data-Structures/Stack/) |
| **Tree** | `39` | Binary Tree creation, Traversals (**Inorder**, **Preorder**, **Postorder**, **Level Order**), Binary Search Tree CRUD (**Insert**, **Search**, **Delete**, **Min Value**), Balanced Tree problems (LC 100, 101, 104, 110, 111, 124, 543, 687), BST Problems (LC 230, 235, 430, 700, 701, 1008, 1382), and Tree Recursion problems (LC 100, 101, 102, 104, 110, 112, 113, 226, 257, 543, 563, 617, 687, 1448). | [📂 Tree](./Data-Structures/Tree/) |

#### 🗺️ Graph 6-Phase Mastery Roadmap
The graph module features an engineered progression strategy documented in [`Data-Structures/GraphDataStructure/ProblemOrder.txt`](./Data-Structures/GraphDataStructure/ProblemOrder.txt):

```text
PHASE 1: Graph Basics        (1971 → 733 → 200 → 695 → 547 → 841)
         ↓
PHASE 2: BFS & Grid Search   (994 → 542 → 1091 → 752 → 127 → 1926 → 934)
         ↓
PHASE 3: Graph DFS           (133 → 797 → 785 → 886 → 802 → 207)
         ↓
PHASE 4: Topological Sort    (207 → 210 → 802 → 2115 → 310)
         ↓
PHASE 5: Shortest Path       (743 → 1514 → 1631 → 787 → 1976)
         ↓
PHASE 6: Disjoint Set (DSU)  (684 → 1319 → 721 → 990 → 1584)
```

---

### 3. Daily Contest Solutions (20 Files)

Solutions to dynamic weekly, biweekly, and daily competitive challenges:

- [📂 DailyContest Directory](./DailyContest/)
  - `Problem 1081.py` - Smallest Subsequence of Distinct Characters
  - `Problem 1331.py` - Rank Transform of an Array
  - `Problem 1358.py` - Number of Substrings Containing All Three Characters
  - `Problem 1846.py` - Maximum Element After Decreasing and Rearranging
  - `Problem 1927.py` - Sum Game
  - `Problem 1967.py` - Number of Strings That Appear as Substrings in Word
  - `Problem 1979.FindGCD.py` - Find Greatest Common Divisor of Array
  - `Problem 2958.py` - Length of Longest Subarray With at Most K Frequency
  - `Problem 3020.py` - Find the Maximum Number of Elements in Subset
  - `Problem 3069.py` - Distribute Elements Into Two Arrays I
  - `Problem 3090.py` - Maximum Length Substring With Two Occurrences
  - `Problem 3345.py` - Smallest Divisible Digit Product I
  - `Problem 3720.py` to `Problem 3904.py` - Recent Contest Challenges

---

### 4. Revision & Rapid Recall (5 Files)

Curated high-frequency problems for pre-interview revision and speed coding:

- [📂 Revision Directory](./Revision/)
  - `26.Remove the duplicate from the sorted array.py` (LC 26)
  - `Moves Zeroes.py` (LC 283)
  - `TwoSum.py` (LC 1)
  - `Valid Anagram.py` (LC 242)
  - `problem Sequence.txt` - Curated high-priority interview sequence:
    `26, 167, 125, 344, 27, 15, 643, 3, 204, 1004, 20, 115, 496, 739, 853, 704, 35, 34, 153, 33`

---

### 5. Java Revision & Practice (13 Files)

Core language mechanics, object-oriented design, and advanced features in Java:

| Topic | Description | Files | Explore |
| :--- | :--- | :---: | :---: |
| **Access Modifiers** | Encapsulation, scope boundaries (private, default, protected, public). | `1` | [📂 AccessModifiers](./JavaRevisionAndPractice/AccessModifiers/) |
| **Advance Java** | Lambdas, Stream API pipelines, Custom `Comparator` and `Comparable` contracts, driver demos. | `5` | [📂 AdvanceJava](./JavaRevisionAndPractice/AdvanceJava/) |
| **Collection Framework** | Dynamic resizing, iteration protocols, `ArrayList` and `List` implementations. | `2` | [📂 CollectionFramework](./JavaRevisionAndPractice/CollectionFramework/) |
| **OOPS Concepts** | Chapter-by-chapter implementations of Inheritance, Polymorphism, Abstraction, and Interfaces. | `3` | [📂 OOPSConcepts](./JavaRevisionAndPractice/OOPSConcepts/) |
| **Method Types** | Direct comparisons between `StaticMethod.java` (class-level) and `InstanceMethod.java` (heap-allocated object state). | `2` | [📂 Java Root](./JavaRevisionAndPractice/) |

---

### 6. Python Fundamentals & OOP (16 Files)

Modularized Python study guides and top coding interview problems:

| Topic | Description | Files | Explore |
| :--- | :--- | :---: | :---: |
| **OOP Principles** | Five-chapter guide: Classes & Objects (`Ch1`), Methods & Attributes (`Ch2`), Inheritance & `super()` (`Ch3`), Encapsulation & Scope (`Ch4`), Polymorphism & Dunder Methods (`Ch5`). | `5` | [📂 OopsConcept](./PythonFundamentalsAndOOP/OopsConcept/) |
| **Python Data Structures** | Built-in data types, dictionary idioms, set optimizations, tuple unpacking. | `1` | [📂 PythonDataStructure](./PythonFundamentalsAndOOP/PythonDataStructure/) |
| **LeetCode Interview Revision** | 10 quintessential coding interview questions (Two Sum, Stock Buy/Sell, Palindrome Number, Valid Palindrome, Valid Parentheses, Reverse String, Remove Duplicates, Find All Duplicates, Majority Element, Fibonacci). | `10` | [📂 LeetCode Revision](./PythonFundamentalsAndOOP/RevisionLeetcodeInterviewQuestion/) |

---

## 📋 Boilerplate Templates & Roadmaps

To accelerate solving new problems without reinventing basic setup code, review the dedicated template and roadmap files:
- **Backtracking Template:** [`Algorithms/Backtracking/templet.txt`](./Algorithms/Backtracking/templet.txt)
- **DFS Template:** [`Algorithms/DFS/templete.txt`](./Algorithms/DFS/templete.txt)
- **Monotonic Stack Template:** [`Algorithms/Monotonic-Stack/templete.txt`](./Algorithms/Monotonic-Stack/templete.txt)
- **Sliding Window Template:** [`Algorithms/Sliding-Window/templete.txt`](./Algorithms/Sliding-Window/templete.txt)
- **Graph Progression Roadmap:** [`Data-Structures/GraphDataStructure/ProblemOrder.txt`](./Data-Structures/GraphDataStructure/ProblemOrder.txt)
- **Stack Problem Roadmap:** [`Data-Structures/Stack/Problem.txt`](./Data-Structures/Stack/Problem.txt)
- **Queue Problem Roadmap:** [`Data-Structures/QueueDataStructure/Problems/Problem.txt`](./Data-Structures/QueueDataStructure/Problems/Problem.txt)
- **Fast-Track Revision Sequence:** [`Revision/problem Sequence.txt`](./Revision/problem Sequence.txt)

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.8+**
- **Java SE Development Kit (JDK) 8 or higher**
- Git (optional, for version control)

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Priy4n5hu21072005/DSA.git
   ```
2. **Navigate into the directory:**
   ```bash
   cd DSA
   ```

---

## 🛠️ Running Solutions

### Python
Any Python solution file can be run directly using the Python interpreter:
```bash
# Run a specific algorithm solution
python Algorithms/Two-Pointers/p11.py

# Run a Graph traversal
python "Data-Structures/GraphDataStructure/Traversal/Shortest path/Dijkstra Algorithm.py"

# Run a Revision problem
python Revision/TwoSum.py
```

### Java
Navigate to the directory of the target Java file, compile, and execute:
```bash
# Compile and run Static vs Instance method demo
cd JavaRevisionAndPractice
javac StaticMethod.java
java StaticMethod

# Compile and run Advance Java Comparator
cd AdvanceJava
javac Comparater.java
java Comparater
```

> [!TIP]
> Each `.py` and `.java` file contains problem statements, input test cases, or explanatory conceptual notes directly in the code comments for seamless self-study!

---

## 🤝 Contributing

Contributions, edge-case solutions, and time/space optimizations are welcome:
1. **Fork** the repository.
2. Create your feature branch:
   ```bash
   git checkout -b feature/AddOptimalSolution
   ```
3. Commit your changes with clear messages:
   ```bash
   git commit -m 'feat: Add Dijkstra shortest path optimization'
   ```
4. Push to your branch:
   ```bash
   git push origin feature/AddOptimalSolution
   ```
5. Open a **Pull Request** detailing the problem number, approach, and time/space complexity.

---

## 📄 License

This repository is self-curated, maintained, and open-source under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use these implementations for personal study, interview preparation, and competitive programming practice. Happy Coding! 💻

