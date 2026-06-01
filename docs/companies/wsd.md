---
description: WSD interview questions, WSD interview stages, WSD interview details, WSD interview question and answers
head:
  - - link
    - rel: canonical
      href: https://tamimehsan.github.io/interview-questions-bangladesh/companies/wsd
---
# WSD

| <img width="441" height="1"> | <img width="441" height="1"> |
| :-| :- |
| Founding year | |
| Company Website | https://wsd.com/ |
| Career Website | https://wsd.com/career/ |
| Technologies Used| Java, Spring Boot, OOP |

## Introduction
[WSD](https://wsd.com/) or Wall Street Docs is a US based company trying to expand in Bangladesh. 

> [!TIP]
> WSD most probably works with Java like Therap BD. So their interview questions generally contains topics from Java, Spring Boot and OOP.

## Interview Stages

At first apply through their [website](https://wsd.bamboohr.com/careers). Apply to the positions located in bangladesh.  
They take their interview in two phases. 
1. **First round** is task based. An assignment will be sent to your email if resume screening is passed.
1. **Second round** is in their Bangladesh office. It is a mix of coding and technical

## First Round Questions
<article>

Create a java console based movie listing application. Features include authentication (signin, login), adding movies, searching movies etc.

<details><summary>Theory and explanation</summary>

WSD's **first-round take-home** is a **console CRUD app** in Java — similar to Therap-style assignments. Interviewers evaluate **OOP structure**, **layering**, and whether features are complete without a GUI.

**Suggested modules**

| Layer | Responsibility |
|-------|----------------|
| **Model** | `User`, `Movie` (id, title, genre, rating, …) |
| **Repository** | In-memory `Map` or file/JSON persistence (`save`/`load`) |
| **Service** | `AuthService` (register/login), `MovieService` (add/search/list) |
| **UI** | `Main` menu loop reading `Scanner` input |

**Authentication**

- Store **hashed passwords** (`BCrypt` or `MessageDigest` + salt) — never plain text.
- Session: logged-in `User` reference in memory after successful login.
- Commands gated: only authenticated users add/search private lists if required.

**Movie features**

- **Add** — validate non-empty title, unique id.
- **Search** — by title substring, genre, or id.
- **List** — all movies or user's watchlist if extended.

**Interview talking points**

- Use **interfaces** for repositories to show testability.
- Mention **exception handling** for invalid menu choices.
- Optional: **JUnit** tests for `MovieService`.
- Package layout: `com.wsd.movies.{model,repo,service,ui}`.

#### Further reading

- [Oracle: The Java Tutorials — Collections](https://docs.oracle.com/javase/tutorial/collections/) — in-memory storage
- [Spring Security: Password encoding](https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html) — hashing practices (even for console apps)
- [Refactoring Guru: Repository pattern](https://refactoring.guru/design-patterns/repository) — layering

</details>

<details><summary>Solution (JavaScript)</summary>

Structural outline in Java (console apps are Java in the assignment; pseudocode for clarity):

```java
// Movie.java
public class Movie {
  private final String id;
  private String title;
  private String genre;
  // getters/setters, constructor
}

// MovieRepository.java
public interface MovieRepository {
  void save(Movie m);
  Optional<Movie> findById(String id);
  List<Movie> searchByTitle(String q);
}

// AuthService.java — register/login with hashed password map
// MovieService.java — add/search delegating to repository
// Main.java — menu: 1 Login 2 Register 3 Add Movie 4 Search 5 List 0 Exit
```

#### Code walkthrough

1. **Model** entities stay free of `Scanner` I/O.
2. **Repository** hides storage; swap `InMemoryMovieRepository` for file later.
3. **Service** enforces rules (duplicate id, auth required).
4. **Main** only parses input and calls services.

#### Complexity

| | |
|-|-|
| Time | Search by title O(n) over in-memory list; hash map by id O(1) |
| Space | O(movies + users) |

#### Edge cases

- **Empty search query** — return all or prompt again.
- **Duplicate username on register** — reject with message.
- **Data loss on exit** — persist to JSON file if assignment expects durability.

</details>

</article>

<article>

Create a java console based banking application. Features include creating, displaying, searching, updating and deleting an account, depositing and withdrawing an amount to your account.

<details><summary>Theory and explanation</summary>

The **banking console app** tests **CRUD**, **transaction integrity**, and **validation** — core skills before Spring Boot onsite questions.

**Account model**

- `accountNumber` (unique), `holderName`, `balance` (`BigDecimal` in Java — never `float` for money).

**Operations**

| Operation | Rules |
|-----------|--------|
| **Create** | Unique account number; initial balance ≥ 0 |
| **Display / Search** | By account number or holder name |
| **Update** | Change holder name; not balance directly (use deposit/withdraw) |
| **Delete** | Remove account if policy allows; confirm zero balance |
| **Deposit / Withdraw** | Amount > 0; withdraw fails if insufficient funds |

**Design**

- `AccountRepository` + `BankingService` with atomic in-memory updates.
- For thread-safety mention `synchronized` or `ConcurrentHashMap` if asked.

**Interview talking points**

- **Audit log** optional: list of transactions per account.
- **Idempotency** not required for console but shows maturity if discussed.
- Align naming with assignment: "acount" in prompt is typo for **account**.

#### Further reading

- [Java BigDecimal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/math/BigDecimal.html) — monetary arithmetic
- [Martin Fowler: Transaction Script vs Domain Model](https://martinfowler.com/eaaCatalog/transactionScript.html) — simple service layering
- [Effective Java: Item 6 — avoid float for money](https://www.oracle.com/java/technologies/effective-java.html) — best practice

</details>

<details><summary>Solution (JavaScript)</summary>

```java
public class Account {
  private final String accountNumber;
  private String holderName;
  private BigDecimal balance = BigDecimal.ZERO;
}

public class BankingService {
  private final Map<String, Account> accounts = new HashMap<>();

  public void createAccount(String no, String name, BigDecimal initial) {
    if (accounts.containsKey(no)) throw new IllegalArgumentException("exists");
    if (initial.compareTo(BigDecimal.ZERO) < 0) throw new IllegalArgumentException("negative");
    accounts.put(no, new Account(no, name, initial));
  }

  public void withdraw(String no, BigDecimal amount) {
    Account a = require(no);
    if (amount.compareTo(BigDecimal.ZERO) <= 0) throw new IllegalArgumentException("amount");
    if (a.getBalance().compareTo(amount) < 0) throw new IllegalStateException("insufficient");
    a.setBalance(a.getBalance().subtract(amount));
  }
  // deposit, update, delete, search similarly
}
```

#### Code walkthrough

- **BigDecimal** for deposit/withdraw avoids rounding bugs.
- **withdraw** checks balance before mutation — atomic in single-threaded app.
- **delete** should refuse non-zero balance unless forcing closure.

#### Complexity

| | |
|-|-|
| Time | O(1) per op with hash map by account number |
| Space | O(accounts) |

#### Edge cases

- **Withdraw exact balance** — allowed, balance becomes zero.
- **Update account number** — usually forbidden; create new account instead.
- **Concurrent access** — not required in take-home unless specified.

</details>

</article>

## Second Round Questions
<article>

Describe key features of spring boot.

<details><summary>Theory and explanation</summary>

**Spring Boot** is an opinionated layer on **Spring Framework** for building production-ready Java applications with minimal boilerplate.

**Key features to mention**

1. **Auto-configuration** — classpath-driven beans (e.g. `DataSource` when JDBC on classpath); reduces XML/Java config.
2. **Starter dependencies** — `spring-boot-starter-web`, `starter-data-jpa` bundle compatible libraries.
3. **Embedded servers** — Tomcat/Jetty/Undertow embedded; run as `java -jar app.jar`.
4. **Production-ready Actuator** — health, metrics, env endpoints (`/actuator/health`).
5. **Externalized configuration** — `application.properties` / `application.yml`, profiles (`dev`, `prod`).
6. **Spring Initializr** — project bootstrap with chosen dependencies.
7. **DevTools** — hot reload for faster local dev (optional mention).

**vs plain Spring**

- Faster bootstrap, sensible defaults, less XML.
- Still uses **DI**, **AOP**, **MVC**, **Data**, **Security** modules.

**Interview talking points**

- Explain **conditional beans** behind auto-config.
- Mention **@SpringBootApplication** = `@Configuration` + `@EnableAutoConfiguration` + `@ComponentScan`.
- WSD onsite may tie this to projects on your resume.

#### Further reading

- [Spring Boot documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/) — official feature list
- [Spring Boot: How it works (auto-config)](https://docs.spring.io/spring-boot/docs/current/reference/html/using.html#using.auto-configuration) — internals overview
- [Baeldung: Spring Boot intro](https://www.baeldung.com/spring-boot) — tutorial-style summary

</details>

<details><summary>Solution (JavaScript)</summary>

Minimal Boot entry (Java — reference structure):

```java
@SpringBootApplication
public class WsdApplication {
  public static void main(String[] args) {
    SpringApplication.run(WsdApplication.class, args);
  }
}

@RestController
class HelloController {
  @GetMapping("/hello")
  String hello() { return "ok"; }
}
```

`application.yml` excerpt:

```yaml
server:
  port: 8080
spring:
  profiles:
    active: dev
```

#### Code walkthrough

- `@SpringBootApplication` triggers component scan and auto-config.
- `spring-boot-starter-web` adds MVC + embedded Tomcat without manual setup.
- Profiles switch beans/config per environment.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Overriding auto-config** — exclude with `@SpringBootApplication(exclude = …)` when custom `DataSource` needed.
- **Fat JAR vs WAR** — Boot defaults to executable JAR; WAR deployment still supported.

</details>

</article>

<article>

What is JWT token? What are the parts of a jwt token?

<details><summary>Theory and explanation</summary>

A **JSON Web Token (JWT)** is a compact, URL-safe string format (RFC 7519) for carrying **claims** between parties, commonly used as a **stateless bearer token** after login.

**Three parts (dot-separated Base64URL)**

1. **Header** — algorithm & type, e.g. `{"alg":"HS256","typ":"JWT"}`.
2. **Payload** — claims: registered (`iss`, `sub`, `exp`, `iat`), public, or private custom (`roles`, `tenant`).
3. **Signature** — `sign(base64url(header) + "." + base64url(payload), secret_or_private_key)` ensures integrity; verifier checks with shared secret or **public key (RS256)**.

**Flow**

1. User authenticates → server issues JWT.
2. Client sends `Authorization: Bearer <token>` on API calls.
3. Resource server validates signature + `exp` (+ `aud`, `iss`).

**Security notes**

- Payload is **encoded, not encrypted** — do not store secrets in JWT.
- Use **HTTPS**; short **TTL**; refresh tokens for revocation challenges.
- Prefer **RS256** when multiple services verify tokens.

#### Further reading

- [JWT.io Introduction](https://jwt.io/introduction) — structure and debugger
- [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519) — specification
- [OWASP: JSON Web Token Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html) — hardening

</details>

<details><summary>Solution (JavaScript)</summary>

Decode structure (verify signature in production with library):

```js
function parseJwt(token) {
  const [headerB64, payloadB64, signature] = token.split('.');
  if (!headerB64 || !payloadB64 || !signature) {
    throw new Error('invalid JWT format');
  }
  const decode = (s) => JSON.parse(Buffer.from(s, 'base64url').toString('utf8'));
  return {
    header: decode(headerB64),
    payload: decode(payloadB64),
    signature, // verify with secret/public key — never trust payload alone
  };
}

// Example payload claims after login:
// { "sub": "user123", "roles": ["USER"], "iat": 1710000000, "exp": 1710003600 }
```

Spring Boot validation (outline):

```java
// spring-boot-starter-oauth2-resource-server
// SecurityFilterChain validates JWT from Authorization header via JWK Set URI
```

#### Code walkthrough

1. Split on `.` into three segments.
2. Base64URL-decode header/payload JSON for inspection only.
3. **Signature** must be verified before trusting claims (`exp`, `roles`).

#### Complexity

| | |
|-|-|
| Time | O(1) verify per request with cached keys |
| Space | O(1) token size (keep claims small) |

#### Edge cases

- **Expired token** — reject when `exp < now`.
- **Algorithm none attack** — whitelist allowed algs server-side.
- **Clock skew** — allow small leeway in `exp`/`nbf` checks.

</details>

</article>

<article>

Given a 2D matrix where each row is sorted. Describe how to find an element in the matrix. What is the complexity of such approach?

<details><summary>Theory and explanation</summary>

Assume an `m × n` matrix where **each row is sorted ascending** (columns may **not** be sorted globally). This is **not** fully sorted matrix search (that uses corner binary search variant).

**Staircase search (top-right or bottom-left)**

- Start at **top-right** `(0, n-1)` (or bottom-left `(m-1, 0)`).
- Compare `matrix[i][j]` with `target`:
  - If **equal** → found.
  - If **greater** → move **left** (`j--`) because all elements to the right in row are larger.
  - If **smaller** → move **down** (`i++`) because all elements above in column are smaller (within row sort).
- Stop when out of bounds → not found.

**Complexity:** **O(m + n)** time, **O(1)** extra space.

**Why not binary search each row only?**

- Row-by-row binary search is **O(m log n)** — acceptable but staircase is simpler and optimal for this constraint set.

**Interview talking points**

- Clarify if **rows and columns** both sorted (LeetCode 240) — then start corner differs slightly but same O(m+n) idea.
- Draw 3×3 example and walk target comparisons.

#### Further reading

- [LeetCode 240: Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) — classic problem
- [GeeksforGeeks: Search row-wise column-wise sorted matrix](https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/) — staircase method
- [VisuAlgo: Binary search variants](https://visualgo.net/en/binarysearch) — intuition

</details>

<details><summary>Solution (JavaScript)</summary>

```js
function searchMatrix(matrix, target) {
  if (!matrix.length || !matrix[0].length) return false;
  let i = 0;
  let j = matrix[0].length - 1;

  while (i < matrix.length && j >= 0) {
    const val = matrix[i][j];
    if (val === target) return true;
    if (val > target) j--;
    else i++;
  }
  return false;
}
```

#### Code walkthrough

1. Begin top-right — largest in first row, can eliminate column or row each step.
2. Each move decreases remaining search space by one row or column.
3. At most `m + n` steps.

#### Complexity

| | |
|-|-|
| Time | O(m + n) |
| Space | O(1) |

#### Edge cases

- **Empty matrix** — return false immediately.
- **Duplicate values** — algorithm still finds one occurrence.
- **Fully sorted matrix (LeetCode 74)** — can use O(log(mn)) binary search on virtual array.

</details>

</article>

<article>

Given a graph G and two nodes u and v of the graph. Find the lowest common ancestor of u and v.

<details><summary>Theory and explanation</summary>

The **Lowest Common Ancestor (LCA)** of nodes `u` and `v` in a rooted tree/graph is the **deepest** node that is an ancestor of both.

**If G is a binary tree (general)**

- **Parent-pointer + hash set:** walk `u` to root storing visited set; walk `v` until hit set — **O(h)** time, **O(h)** space.
- **Binary lifting / Euler tour + RMQ:** preprocess for **O(log n)** or **O(1)** per query — mention for many queries.

**If G is a DAG or general graph**

- Clarify definition — may need **all paths** or treat as tree after rooting; LCA is standard on **trees**.

**If G is a Binary Search Tree**

- Compare values: if `u.val < root.val && v.val < root.val` → LCA in left subtree; if both greater → right; else **root** is LCA — **O(h)**.

**Interview talking points**

- Ask: **rooted tree?** BST? **Multiple queries?**
- WSD may accept BST solution if they say "graph" loosely — explain both.

#### Further reading

- [LeetCode 236: LCA of Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) — pointer walk
- [LeetCode 235: LCA of BST](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) — value compare
- [CP-Algorithms: LCA](https://cp-algorithms.com/graph/lca.html) — binary lifting

</details>

<details><summary>Solution (JavaScript)</summary>

Binary tree (parent pointers via parent map):

```js
function lowestCommonAncestor(root, p, q) {
  const ancestors = new Set();
  let cur = p;
  while (cur) {
    ancestors.add(cur);
    cur = cur.parent; // or build parent map via DFS first
  }
  cur = q;
  while (cur) {
    if (ancestors.has(cur)) return cur;
    cur = cur.parent;
  }
  return null;
}

// BST variant
function lcaBST(root, p, q) {
  let node = root;
  while (node) {
    if (p.val < node.val && q.val < node.val) node = node.left;
    else if (p.val > node.val && q.val > node.val) node = node.right;
    else return node;
  }
  return null;
}
```

Recursive tree (no parent field):

```js
function lca(root, p, q) {
  if (!root || root === p || root === q) return root;
  const left = lca(root.left, p, q);
  const right = lca(root.right, p, q);
  if (left && right) return root;
  return left || right;
}
```

#### Code walkthrough

- **Recursive:** if both subtrees return non-null, current node is LCA.
- **BST:** use ordering to walk one path from root.
- **Hash set:** collect `p` ancestors, scan `q` upward.

#### Complexity

| | |
|-|-|
| Time | O(h) tree height; O(n) worst skewed tree |
| Space | O(h) recursion or ancestor set |

#### Edge cases

- **`p` is ancestor of `q`** — return `p`.
- **Disconnected graph** — LCA undefined; clarify with interviewer.

</details>

</article>

<article>

What are the key points of OOP?

<details><summary>Theory and explanation</summary>

Object-Oriented Programming organizes software around **objects** combining **data** and **behavior**.

**Four pillars**

1. **Encapsulation** — hide internal state; expose methods (`private` fields, public API).
2. **Abstraction** — show essential behavior; hide implementation (`interface`, abstract class).
3. **Inheritance** — reuse/extend behavior (`extends`); **favor composition over inheritance** when possible.
4. **Polymorphism** — one interface, many implementations (method **overriding** runtime; **overloading** compile-time).

**Additional principles interviewers like**

- **SOLID** (SRP, OCP, LSP, ISP, DIP).
- **Coupling vs cohesion** — modules should be focused and loosely coupled.
- **Immutable value objects** where appropriate.

**Java mapping**

- `class`, `interface`, `abstract class`, `@Override`, access modifiers.

#### Further reading

- [Oracle: What Is an Object?](https://docs.oracle.com/javase/tutorial/java/concepts/) — Java OOP basics
- [Refactoring Guru: OOP basics](https://refactoring.guru/design-patterns/what-is-design-patterns) — pillars explained
- [SOLID principles (Uncle Bob)](https://blog.cleancoder.com/uncle-bob/2020/10/18/Solid-Relevance.html) — design quality

</details>

<details><summary>Solution (JavaScript)</summary>

Polymorphism example (language-agnostic):

```js
class Shape {
  area() { throw new Error('implement'); }
}
class Circle extends Shape {
  constructor(r) { super(); this.r = r; }
  area() { return Math.PI * this.r * this.r; }
}
class Rect extends Shape {
  constructor(w, h) { super(); this.w = w; this.h = h; }
  area() { return this.w * this.h; }
}

function totalArea(shapes) {
  return shapes.reduce((sum, s) => sum + s.area(), 0);
}
```

#### Code walkthrough

- **Abstraction:** `Shape` defines contract.
- **Encapsulation:** radius inside `Circle`.
- **Polymorphism:** `totalArea` calls correct `area()` per runtime type.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Deep inheritance hierarchies** — fragile; prefer interfaces + composition.
- **Violating LSP** — subclass breaks parent expectations (classic interview trap).

</details>

</article>

<article>

Describe abstract class and interface. What are their similarities and dissimilarities? What are their benefits?

<details><summary>Theory and explanation</summary>

| | **Abstract class** | **Interface** |
|---|-------------------|---------------|
| **Instantiation** | Cannot `new` directly | Cannot `new` directly |
| **Fields** | Can have instance fields, constructors | Java 8+: `default`/`static` methods; fields are `public static final` |
| **Methods** | Abstract + concrete methods | Abstract (implicit) + `default`/`static` (Java 8+) |
| **Inheritance** | Class **extends** one abstract class | Class **implements** multiple interfaces |
| **Purpose** | Shared **base implementation** + partial contract | **Capability contract** across unrelated types |

**Similarities**

- Define types that are incomplete until subclassed/implemented.
- Enable **polymorphism** via superclass/interface references.
- Support **design by contract**.

**Benefits**

- **Abstract class:** DRY for common code (`AbstractRepository` with shared CRUD).
- **Interface:** Multiple behaviors (`Serializable`, `Comparable`); easier mocking in tests.
- **Java 21+** — interfaces can have private methods for default method helpers.

**When to use which**

- Shared state + template method pattern → **abstract class**.
- Cross-cutting roles, API boundaries → **interface**.

#### Further reading

- [Oracle: Abstract classes vs interfaces](https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html) — official guidance
- [Effective Java: Item 20 — prefer interfaces](https://www.oracle.com/java/technologies/effective-java.html) — design advice
- [Baeldung: Interface vs abstract class](https://www.baeldung.com/java-abstract-class-vs-interface) — comparison table

</details>

<details><summary>Solution (JavaScript)</summary>

Java-style sketch:

```java
abstract class BaseRepository<T, ID> {
  protected final Map<ID, T> store = new HashMap<>();
  public T findById(ID id) { return store.get(id); }
  abstract void validate(T entity);
}

interface Auditable {
  Instant createdAt();
  void touch();
}

class UserRepository extends BaseRepository<User, Long> implements Auditable {
  void validate(User u) { /* ... */ }
  public Instant createdAt() { return Instant.now(); }
  public void touch() { /* audit */ }
}
```

#### Code walkthrough

- **Abstract class** provides `findById` implementation + forces `validate`.
- **Interface** adds orthogonal `Auditable` without tying inheritance tree.
- Class can **extend one** abstract class and **implement many** interfaces.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Diamond problem** — Java disallows multiple class inheritance; interfaces + default methods need careful override rules.
- **Empty interface** — discouraged; use annotations or minimal methods.

</details>

</article>

<article>

Describe key features of spring boot.

<details><summary>Theory and explanation</summary>

@@info:This question appears twice in reported WSD onsite loops — prepare the same talking points consistently.@@

See the enriched answer in the first **Describe key features of spring boot** question above: auto-configuration, starters, embedded server, Actuator, externalized config, profiles, and `@SpringBootApplication` composition.

**Extra onsite depth**

- **Spring Boot 3** — Jakarta EE namespace (`jakarta.*`), native image support (GraalVM) optional mention.
- **Testing:** `@SpringBootTest`, `@WebMvcTest`, Testcontainers for integration tests.
- **Data access:** `spring-boot-starter-data-jpa` + HikariCP pool auto-config.

#### Further reading

- [Spring Boot 3 migration guide](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-3.0-Migration-Guide) — Jakarta changes
- [Spring Boot Testing](https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.testing) — test slices

</details>

<details><summary>Solution (JavaScript)</summary>

Quick revision checklist (no code required onsite):

```text
✓ Auto-config + conditional beans
✓ Starters (web, data-jpa, security)
✓ Embedded Tomcat + java -jar
✓ application.yml + profiles
✓ Actuator health/metrics
✓ @RestController + @Service + @Repository layering
```

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

</details>

</article>

<article>

What happens when final keyword is used with variables and classes?

<details><summary>Theory and explanation</summary>

In **Java**, `final` restricts modification depending on where it is applied.

**`final` variable (local, field, parameter)**

- Must be **assigned once** before use (for fields: in declaration, instance initializer, or every constructor).
- For primitives — value cannot change; for references — **reference** cannot be reassigned (object state may still mutate unless immutable).
- **`final` parameters** — cannot reassign inside method; useful for anonymous inner classes (legacy) and clarity.

**`final` method**

- Cannot be **overridden** by subclasses (allows JVM devirtualization optimizations).

**`final` class**

- Cannot be **extended** — e.g. `String`, wrapper classes; use when invariants must not be broken by subclassing.

**`final` vs immutability**

- `final List<String> list` — list reference fixed; `list.add()` still allowed unless list is immutable implementation.

**Interview talking points**

- Contrast with **`const` in C++** / **`const` in JS** (different semantics).
- Mention **blank final** instance fields set in constructor.

#### Further reading

- [Oracle: final variables](https://docs.oracle.com/javase/tutorial/java/IandI/final.html) — official tutorial
- [Effective Java: Minimize mutability](https://www.oracle.com/java/technologies/effective-java.html) — `final` fields in immutable classes
- [JLS: final fields](https://docs.oracle.com/javase/specs/jls/se17/html/jls-4.html#jls-4.12.4) — memory model visibility

</details>

<details><summary>Solution (JavaScript)</summary>

Java examples:

```java
final int MAX = 100;           // constant-like
final StringBuilder sb = new StringBuilder("a");
sb.append("b");                // OK — mutate object
// sb = new StringBuilder();   // compile error — reassign reference

final class Utility {          // cannot extend
  static int add(int a, int b) { return a + b; }
}

class Parent {
  final void doWork() {}       // cannot override
}
```

#### Code walkthrough

- **Variable:** one assignment to binding; object mutability separate.
- **Class:** inheritance blocked — security for sensitive types.
- **Method:** override blocked — template method safety.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Finalizer method** `finalize()` — deprecated; not related to `final` keyword.
- **Blank final without constructor assignment** — compile error.

</details>

</article>

<article>

Given a binary search tree, find/ insert an element in the tree

<details><summary>Theory and explanation</summary>

A **Binary Search Tree (BST)** satisfies: for every node, **left subtree keys < node.key < right subtree keys** (assuming distinct keys; duplicates handled by convention).

**Search**

- Start at root; if target == node.key return; if less go left, else right; **O(h)**.

**Insert**

- Same walk as search; when `null` child reached, attach new node — **O(h)**.

**Height**

- Balanced BST **h = O(log n)**; skewed chain **h = O(n)**.

**Interview talking points**

- Mention **iterative vs recursive** implementations.
- After many inserts, suggest **AVL/Red-Black** tree or `TreeMap` in Java for balance.
- Deletion (not asked but good bonus): three cases — leaf, one child, two children (successor).

#### Further reading

- [LeetCode 700: Search in BST](https://leetcode.com/problems/search-in-a-binary-search-tree/) — search
- [LeetCode 701: Insert into BST](https://leetcode.com/problems/insert-into-a-binary-search-tree/) — insert
- [CLRS: Binary search trees](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/) — formal analysis

</details>

<details><summary>Solution (JavaScript)</summary>

```js
class Node {
  constructor(key) {
    this.key = key;
    this.left = null;
    this.right = null;
  }
}

function search(root, key) {
  let cur = root;
  while (cur) {
    if (key === cur.key) return cur;
    cur = key < cur.key ? cur.left : cur.right;
  }
  return null;
}

function insert(root, key) {
  if (!root) return new Node(key);
  let cur = root;
  while (true) {
    if (key === cur.key) return root; // duplicate policy: ignore
    if (key < cur.key) {
      if (!cur.left) { cur.left = new Node(key); return root; }
      cur = cur.left;
    } else {
      if (!cur.right) { cur.right = new Node(key); return root; }
      cur = cur.right;
    }
  }
}
```

#### Code walkthrough

1. **Search** follows BST ordering at each node.
2. **Insert** finds parent position and links new leaf.
3. Duplicate key policy stated explicitly (ignore or count in left subtree).

#### Complexity

| | |
|-|-|
| Time | O(h) per operation |
| Space | O(1) iterative; O(h) recursive stack |

#### Edge cases

- **Empty tree insert** — new root.
- **Duplicate keys** — clarify required behavior.
- **Integer overflow** — not applicable; use comparable keys consistently.

</details>

</article>

<article>

Describe method overloading and method overriding.

<details><summary>Theory and explanation</summary>

| | **Overloading** | **Overriding** |
|---|-----------------|----------------|
| **Where** | Same class (or varargs/static rules) | Subclass vs superclass |
| **Signature** | Same name, **different parameter list** | Same name + compatible parameter list |
| **Return type** | Can differ (after resolution) | Covariant return allowed (Java) |
| **Binding** | **Compile-time** (static) | **Runtime** (dynamic dispatch) |
| **Access** | Any visibility | Cannot reduce visibility; cannot override `final`/`static` same way |

**Overloading example:** `print(int)`, `print(String)`.

**Overriding example:** `Animal.speak()` → `Dog.speak()` with `@Override`.

**Interview talking points**

- **@Override** annotation catches signature typos.
- **static methods** are hidden, not overridden.
- **Overload resolution** picks most specific applicable method.

#### Further reading

- [Oracle: Overriding and Hiding](https://docs.oracle.com/javase/tutorial/java/IandI/override.html) — official rules
- [Oracle: Overloading](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html) — same-class overloads
- [JLS: Method invocation](https://docs.oracle.com/javase/specs/jls/se17/html/jls-15.html#jls-15.12) — resolution rules

</details>

<details><summary>Solution (JavaScript)</summary>

Java-style equivalent concepts:

```java
// Overloading
class Printer {
  void print(int x) { System.out.println(x); }
  void print(String s) { System.out.println(s); }
}

// Overriding
class Animal { void speak() { System.out.println("?"); } }
class Dog extends Animal {
  @Override void speak() { System.out.println("woof"); }
}

Animal a = new Dog();
a.speak(); // runtime: woof
```

JS does not have true overloads — last function wins; Java WSD expects Java rules above.

#### Code walkthrough

- Overload: compiler picks method from argument types at **compile time**.
- Override: JVM uses **vtable** of actual object type at **runtime**.

#### Complexity

| | |
|-|-|
| Time | N/A (conceptual) |
| Space | N/A (conceptual) |

#### Edge cases

- **Overriding private methods** — not inherited, no override.
- **Generics + overload** — erasure can cause bridge methods (advanced).

</details>

</article>

