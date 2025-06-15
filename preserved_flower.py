RATIOS = {
    'glycerin': 1.5,
    'alcohol': 2.0,
    'silica': 1.2,
}

def compute_required_volume(weight_g: float, liquid_type: str) -> float:
    liquid_type = liquid_type.lower()
    if liquid_type not in RATIOS:
        raise ValueError(f"Unsupported liquid type: {liquid_type}")
    return weight_g * RATIOS[liquid_type]


def main():
    weight = float(input("花の重さ(g)を入力してください: "))
    liquid = input("液体の種類を入力してください (glycerin, alcohol, silica): ")
    volume = compute_required_volume(weight, liquid)
    print(f"必要な液量は {volume} ml です")


if __name__ == "__main__":
    main()
