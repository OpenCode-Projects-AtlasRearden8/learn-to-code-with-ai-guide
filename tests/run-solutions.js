const { spawnSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const solutionsDir = path.join(__dirname, "..", "solutions");
const files = fs
  .readdirSync(solutionsDir)
  .filter((f) => f.endsWith(".js"))
  .sort();

let failures = 0;

for (const file of files) {
  const result = spawnSync(process.execPath, [path.join(solutionsDir, file)], {
    encoding: "utf8",
  });
  const passed = result.status === 0;
  if (!passed) failures += 1;
  console.log(
    `${passed ? "PASS" : "FAIL"}  solutions/${file}${
      passed
        ? ""
        : "\n" + (result.stderr || result.stdout || "no output")
    }`
  );
}

if (files.length === 0) {
  console.log("FAIL  no solution files found");
  failures += 1;
}

console.log(
  failures === 0
    ? "ALL EXERCISE SOLUTIONS PASSED"
    : `${failures} solution file(s) failed`
);
process.exit(failures === 0 ? 0 : 1);
