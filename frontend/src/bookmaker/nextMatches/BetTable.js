import * as React from "react";
import Paper from "@mui/material/Paper";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Button,
} from "@mui/material";

import BetDialog from "./BetDialog";

const BetTable = ({
  homeTeam,
  awayTeam,
  homeOdds,
  awayOdds,
  drawOdds,
  id,
  ...props
}) => {
  return (
    <TableContainer component={Paper} sx={{ p: 1 }}>
      <Table
        sx={{
          maxWidth: "100%",
          "& td, th": { border: 0, fontSize: "16px", p: 1, align: "center" },
        }}
      >
        <TableHead>
          <TableRow>
            <TableCell align="center">{homeTeam}</TableCell>
            <TableCell align="center">Draw</TableCell>
            <TableCell align="center">{awayTeam}</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          <TableRow>
            <TableCell align="center">{homeOdds}/1</TableCell>
            <TableCell align="center">{drawOdds}/1</TableCell>
            <TableCell align="center">{awayOdds}/1</TableCell>
          </TableRow>
          <TableRow>
            <TableCell align="center">
              <BetDialog
                matchId={id}
                choice="HOME"
                odds={homeOdds}
                text={`${homeTeam} to beat ${awayTeam}`}
                trigger={(props) => <BetButton {...props} />}
              />
            </TableCell>
            <TableCell align="center">
              <BetDialog
                matchId={id}
                choice="DRAW"
                odds={drawOdds}
                text={`${homeTeam} to draw with ${awayTeam}`}
                trigger={(props) => <BetButton {...props} />}
              />
            </TableCell>
            <TableCell align="center">
              <BetDialog
                matchId={id}
                choice="AWAY"
                odds={awayOdds}
                text={`${awayTeam} to beat ${homeTeam}`}
                trigger={(props) => <BetButton {...props} />}
              />
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export const BetButton = ({ ...props }) => (
  <Button
    sx={{ height: 10, m: 0, cursor: "pointer" }}
    color="red"
    size="small"
    variant="contained"
    {...props}
  >
    Bet
  </Button>
);
export default BetTable;
