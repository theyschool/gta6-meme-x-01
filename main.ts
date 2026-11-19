// gta6-meme-x-01 entrypoint.
//
// The entry is the X post itself: the meme picture and the post text.
// This program only hands the house the post's address. It reads
// POST.json out of the repository, makes sure it is a JSON object with
// a url string in it, and writes that same file to the output
// directory, where the grader reads it. Nothing about the post is
// judged from what this program writes; the house reads the post
// from X on its own.
//
// Local run:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const sourcePath = join(botDir, "POST.json");
const raw = readFileSync(sourcePath, "utf8");

let parsed: unknown;
try {
  parsed = JSON.parse(raw);
} catch (err) {
  console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
  process.exit(1);
}

if (
  typeof parsed !== "object" ||
  parsed === null ||
  typeof (parsed as { url?: unknown }).url !== "string"
) {
  console.error("POST.json must be an object with a string \"url\" field");
  process.exit(1);
}

const postUrl = (parsed as { url: string }).url;

// The placeholder is not a post's address: the gate refuses it.
// Warn loudly here so a run with the placeholder in place can never
// be mistaken for a finished entry, but still write the file out so
// local runs and checks keep working before the post goes up.
if (postUrl.includes("<") || postUrl.includes(">")) {
  console.error(
    "WARNING: POST.json still holds the placeholder address. " +
      "Replace <id> with the real post id before submitting.",
  );
}

mkdirSync(outDir, { recursive: true });
const destPath = join(outDir, "POST.json");
writeFileSync(destPath, raw);
console.log(`wrote ${destPath} (${raw.length} bytes)`);
