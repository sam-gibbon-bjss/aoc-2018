use std::env;
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let args: Vec<String> = env::args().collect();
    let input_filename = &args[1];

    let mut input_file = File::open(input_filename).expect("File not found");
    let mut input = String::new();
    input_file.read_to_string(&mut input)
        .expect("Failed to read file");

    let input_lines: Vec<i32> = input.split("\n").map(|line| {
        return match line.parse::<i32>() {
            Ok(n) => n,
            Err(_e) => 0,
        };
    }).filter(|&v| v != 0).collect();

    println!("{:?}", input_lines);

    let mut cum_freq = 0;
    let mut found_frequencies: Vec<i32> = Vec::new();

    let mut i = 0;
    'outer: while true {
        for freq in input_lines.clone() {
            cum_freq += freq;
            if found_frequencies.contains(&cum_freq) {
              println!("Found repeated frequency {}", cum_freq);
              break 'outer;
            } else {
              found_frequencies.push(cum_freq);
            }
        }
        i += 1;
        println!("Iter {}, cum_freq {}", i, cum_freq);
    }
}
