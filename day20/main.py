import collections
import dataclasses
import itertools
import re


@dataclasses.dataclass(unsafe_hash=True)
class Coordinate:
    x: int
    y: int
    z: int


@dataclasses.dataclass
class Particle:
    position: Coordinate
    velocity: Coordinate
    acceleration: Coordinate

    def update(self) -> None:
        self.velocity.x += self.acceleration.x
        self.velocity.y += self.acceleration.y
        self.velocity.z += self.acceleration.z

        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        self.position.z += self.velocity.z


def parse_input(input: str) -> list[Particle]:
    particles = re.findall(
        r"p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, a=<(-?\d+),(-?\d+),(-?\d+)>",
        input,
    )

    return [
        Particle(*(Coordinate(*i) for i in itertools.batched(map(int, particle), 3)))
        for particle in particles
    ]


def manhattan_distance_zero(position: Coordinate) -> int:
    return sum(map(abs, (position.x, position.y, position.z)))


def part1(input: str) -> int:
    particles = parse_input(input)

    for _ in range(1000):
        for particle in particles:
            particle.update()

    return min(
        enumerate(particles), key=lambda i: manhattan_distance_zero(i[1].position)
    )[0]


def part2(input: str) -> int:
    particles = parse_input(input)

    for _ in range(1000):
        positions = collections.defaultdict(list)

        for particle in particles:
            particle.update()
            positions[particle.position].append(particle)

        for position in positions:
            if len(positions[position]) > 1:
                for particle in positions[position]:
                    particles.remove(particle)

    return len(particles)


def main() -> None:
    with open("input.txt") as file:
        input = file.read()

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))


if __name__ == "__main__":
    main()
