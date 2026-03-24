import { Mafs, Coordinates, Plot, Point, Vector, Circle, Line, Polygon, Text, Theme } from 'mafs';

interface MafsConfig {
  type: 'cartesian' | 'polar' | 'geometry';
  viewBox?: {
    x: [number, number];
    y: [number, number];
  };
  preserveAspectRatio?: boolean;
  elements: MafsElement[];
}

interface MafsElement {
  type: 'plot' | 'point' | 'vector' | 'circle' | 'line' | 'polygon' | 'text' | 'coordinates';
  // Plot
  function?: string;
  // Point
  coordinates?: [number, number];
  // Vector
  tail?: [number, number];
  tip?: [number, number];
  // Circle
  center?: [number, number];
  radius?: number;
  filled?: boolean;
  fillOpacity?: number;
  // Line
  point1?: [number, number];
  point2?: [number, number];
  style?: 'solid' | 'dashed';
  // Polygon
  points?: [number, number][];
  // Text
  position?: [number, number];
  text?: string;
  // Common
  color?: string;
  label?: string;
  lineWidth?: number;
  // Coordinates
  variant?: 'cartesian' | 'polar';
}

interface MafsRendererProps {
  config: MafsConfig | string;
  className?: string;
}

/**
 * Renders interactive mathematical visualizations using Mafs.js
 * Supports graphs, geometric shapes, vectors, and more
 */
export function MafsRenderer({ config, className = '' }: MafsRendererProps) {
  // Parse config if it's a JSON string
  const parsedConfig: MafsConfig = typeof config === 'string' ? JSON.parse(config) : config;

  const viewBox = parsedConfig.viewBox || { x: [-10, 10], y: [-10, 10] };
  const preserveAspectRatio = parsedConfig.preserveAspectRatio ? 'contain' as const : false as const;

  // Evaluate function strings to actual functions
  const evaluateFunction = (fnString: string): ((x: number) => number) => {
    try {
      // Support various function formats
      if (fnString.startsWith('x =>') || fnString.startsWith('(x)') || fnString.startsWith('function')) {
        // eslint-disable-next-line no-new-func
        return new Function('return ' + fnString)();
      } else {
        // Simple expression like "x**2" or "Math.sin(x)"
        // eslint-disable-next-line no-new-func
        return new Function('x', 'return ' + fnString) as (x: number) => number;
      }
    } catch (e) {
      console.error('Error evaluating function:', fnString, e);
      return () => 0;
    }
  };

  const renderElement = (element: MafsElement, index: number) => {
    const key = `element-${index}`;

    switch (element.type) {
      case 'coordinates':
        return (
          <Coordinates.Cartesian
            key={key}
            subdivisions={4}
            xAxis={{ lines: 1 }}
            yAxis={{ lines: 1 }}
          />
        );

      case 'plot':
        if (!element.function) return null;
        const plotFn = evaluateFunction(element.function);
        return (
          <Plot.OfX
            key={key}
            y={plotFn}
            color={element.color || Theme.blue}
            weight={element.lineWidth || 2}
          />
        );

      case 'point':
        if (!element.coordinates) return null;
        return (
          <Point
            key={key}
            x={element.coordinates[0]}
            y={element.coordinates[1]}
            color={element.color || Theme.red}
          />
        );

      case 'vector':
        if (!element.tail || !element.tip) return null;
        return (
          <Vector
            key={key}
            tail={element.tail}
            tip={element.tip}
            color={element.color || Theme.green}
          />
        );

      case 'circle':
        if (!element.center || element.radius === undefined) return null;
        return (
          <Circle
            key={key}
            center={element.center}
            radius={element.radius}
            strokeStyle={element.style || 'solid'}
            color={element.color || Theme.violet}
            fillOpacity={element.filled ? (element.fillOpacity || 0.2) : 0}
          />
        );

      case 'line':
        if (!element.point1 || !element.point2) return null;
        return (
          <Line.Segment
            key={key}
            point1={element.point1}
            point2={element.point2}
            color={element.color || Theme.orange}
            style={element.style || 'solid'}
          />
        );

      case 'polygon':
        if (!element.points || element.points.length < 3) return null;
        return (
          <Polygon
            key={key}
            points={element.points}
            color={element.color || Theme.pink}
            fillOpacity={element.filled ? (element.fillOpacity || 0.2) : 0}
            strokeStyle={element.style || 'solid'}
          />
        );

      case 'text':
        if (!element.position || !element.text) return null;
        return (
          <Text
            key={key}
            x={element.position[0]}
            y={element.position[1]}
            color={element.color || Theme.foreground}
          >
            {element.text}
          </Text>
        );

      default:
        return null;
    }
  };

  return (
    <div className={`mafs-container my-6 flex justify-center ${className}`}>
      <div className="w-full max-w-[500px]">
        <Mafs
          viewBox={viewBox}
          preserveAspectRatio={preserveAspectRatio}
          height={500}
          width={500}
        >
          {parsedConfig.elements.map((element, index) => renderElement(element, index))}
        </Mafs>
      </div>
    </div>
  );
}

/**
 * Example usage:
 *
 * const config = {
 *   type: 'cartesian',
 *   viewBox: { x: [-5, 5], y: [-5, 5] },
 *   elements: [
 *     { type: 'coordinates' },
 *     { type: 'plot', function: 'x => x**2', color: '#3b82f6' },
 *     { type: 'point', coordinates: [2, 4], color: '#ef4444' },
 *   ]
 * };
 *
 * <MafsRenderer config={config} />
 */
