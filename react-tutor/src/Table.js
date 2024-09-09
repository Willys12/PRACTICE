import React, { Component } from 'react'


const TableHeader = () => {
    return (
        <thead>
            <tr>
                <th>Name</th>
                <th>Job</th>
                <th>Residence</th>
            </tr>
        </thead>
    );
};

const TableBody = () => {
    return (
        <tbody>
            <tr>
                <td>Charlie</td>
                <td>Janitor</td>
                <td>Seattle</td>
            </tr>
            <tr>
                <td>David</td>
                <td>Developer</td>
                <td>New York</td>
            </tr>
            <tr>
                <td>Emily</td>
                <td>Designer</td>
                <td>Los Angeles</td>
            </tr>
            <tr>
                <td>Samson</td>
                <td>CTO</td>
                <td>Chicago</td>
            </tr>
        </tbody>
    );
};
class Table extends Component {
  render () {
    return (
        <table>
            <TableHeader />
            <TableBody />
        </table>
    );
  };
};

export default Table;