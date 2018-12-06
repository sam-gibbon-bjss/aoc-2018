use std::env;
use std::fs::File;
use std::io::prelude::*;

mod part2;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input_filename = &args[1];

    let mut input_file = File::open(input_filename).expect("File not found");
    let mut input = String::new();
    input_file.read_to_string(&mut input)
        .expect("Failed to read file");

    let input_lines = input.split("\n");

    let mut two_count = 0;
    let mut three_count = 0;

    for id in input_lines.clone() {
        let mut letters: Vec<&str> = id.split("").collect();
        letters.sort();
        letters.dedup();

        let mut has_twos = false;
        let mut has_threes = false;

        for letter in letters {
            let letter_count = id.matches(letter).count();
            if letter_count == 2 { has_twos = true; }
            else if letter_count == 3 { has_threes = true; }
        }

        if has_twos { two_count += 1; }
        if has_threes { three_count += 1; }
    }

    println!("Twos: {}\nThrees: {}\nChecksum: {}", two_count, three_count, two_count * three_count);

    part2::part2(input_lines.clone().collect());
}
