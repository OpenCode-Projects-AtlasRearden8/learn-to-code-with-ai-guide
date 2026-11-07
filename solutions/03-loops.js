const captured = [];
const originalLog = console.log;
console.log = (...args) => captured.push(args.join(" "));

const results = [];

function check(label, condition) {
  results.push({ label, ok: Boolean(condition) });
}

console.log("--- 3.1 countdown ---");
for (let i = 5; i >= 1; i--) {
  console.log(i);
}
console.log("Liftoff!");

console.log("--- 3.2 evens ---");
for (let i = 2; i <= 10; i += 2) {
  console.log(i);
}

function sumTo(n) {
  let total = 0;
  for (let i = 1; i <= n; i++) {
    total = total + i;
  }
  return total;
}
console.log("--- 3.3 sum ---");
console.log(sumTo(10));

check("3.1 prints 5,4,3,2,1 then Liftoff", captured.join("\n").includes("5\n4\n3\n2\n1\nLiftoff!"));
check(
  "3.2 prints each even 2..10",
  [2, 4, 6, 8, 10].every((n) => captured.includes(String(n)))
);

check("3.3 sum 1..10 is 55", sumTo(10) === 55);
check("3.3 sum 1..100 is 5050", sumTo(100) === 5050);

console.log = originalLog;
console.log("chapter 03 exercises: outputs above, checks below");

if (results.every((r) => r.ok)) {
  console.log("chapter 03 exercises: all checks ok");
} else {
  console.error(results.filter((r) => !r.ok));
  process.exit(1);
}
