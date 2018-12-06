use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::*;

extern crate edit_distance;

pub fn part2(input_lines: Vec<&str>) {
    let pair = find_pair(input_lines);
    println!("Found pair {} and {}", pair[0], pair[1]);

    let mut letters1: Vec<&str> = pair[0].split("").collect();
    let mut letters2: Vec<&str> = pair[1].split("").collect();

    let mut i = 0;
    while i < pair[0].len() {
        let letter1 = letters1[i];
        let letter2 = letters2[i];

        if letter1 == letter2 {
            i += 1;
            continue;
        }

        println!("Different in position {} ({} and {})", i, letter1, letter2);

        letters1.remove(i);
        letters2.remove(i);

        println!("Common letters: {} (sanity check: {})", letters1.join(""), letters2.join(""));
    }
}

fn find_pair(input_lines: Vec<&str>) -> Vec<&str> {
    for id in input_lines.clone() {
        println!("Checking pairs for {}", id);
        let lines2 = input_lines.clone();

        for id2 in lines2 {
            let distance = edit_distance::edit_distance(id, id2);
            if distance == 1 {
                return vec![id, id2];
            }
        }
    }

    return vec![];
}
