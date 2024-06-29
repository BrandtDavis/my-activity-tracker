import React, { PureComponent, useState, useEffect } from "react";

export default class CustomizedXAxisTick extends PureComponent<{ x: any, y: any, stroke: any, payload: any }> {
    render() {
        const { x, y, stroke, payload } = this.props;
    
        return (
          <g transform={`translate(${x},${y})`}>
            <text x={0} y={0} dy={16} textAnchor="end" fill="#666" transform="rotate(-35)">
              {payload.value}
            </text>
          </g>
        );
      }
}