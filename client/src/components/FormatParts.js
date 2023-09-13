export const formatPart = (key, part) => {
    switch (key) {
      case 'Price':
        return `$${part}`;
      case 'Speed':
        return `${part} MHz`;
      case 'Size': 
        return `${part} TB`;
      case 'Wattage': 
        return `${part} Watt`;
      default:
        return part;
    }
  };

