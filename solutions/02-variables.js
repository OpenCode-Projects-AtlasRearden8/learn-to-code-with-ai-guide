const results = [];

function check(label, condition) {
  results.push({ label, ok: Boolean(condition) });
}

const name = "Dana";
const yearsAtJob = 3;
const hadCoffeeToday = true;

const intro = `Hi, I'm ${name}, I've been at my job ${yearsAtJob} years, and coffee: ${hadCoffeeToday}.`;
console.log(intro);

let total = 0;
total = total + 3;
total = total + 12.25;
console.log(total);
console.log(`With a $2 tip: ${total + 2}`);

const daysInWeek = 7;

check("ex 2.1: name is a string", typeof name === "string");
check("ex 2.1: years is a number", typeof yearsAtJob === "number");
check("ex 2.1: coffee is a boolean", typeof hadCoffeeToday === "boolean");
check("ex 2.1: template literal builds a sentence", intro.includes("Dana"));
check("ex 2.2: running total reaches 15.25", total === 15.25);
check("ex 2.2: tip line adds 2", total + 2 === 17.25);
check(
  "ex 2.3: \"5\" + 1 is \"51\" because the string wins",
  "5" + 1 === "51"
);
check(
  "ex 2.3: const resists reassignment",
  (() => {
    try {
      daysInWeek = 8;
    } catch (err) {
      return err instanceof TypeError;
    }
    return false;
  })()
);

if (results.every((r) => r.ok)) {
  console.log("chapter 02 exercises: all checks ok");
} else {
  console.error(results.filter((r) => !r.ok));
  process.exit(1);
}
