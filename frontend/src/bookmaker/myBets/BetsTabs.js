import React from "react";
import { Stack, Pagination, Button } from "@mui/material";
import ceil from "lodash/ceil";
import ArrowDownwardIcon from "@mui/icons-material/ArrowDownward";
import ArrowUpwardIcon from "@mui/icons-material/ArrowUpward";

import { FETCH_MY_BETS_LIMIT } from "../bookmakerApi";
import BetCard from "./BetCard";
import { Loading, Error } from "src/ui";

const BetsTabs = ({
  betsQuery,
  page,
  handlePageChange,
  toggleOrdering,
  ordering,
}) => {
  const { data, isLoading, isError } = betsQuery;

  if (isLoading) {
    return <Loading />;
  }
  if (isError) {
    return <Error />;
  }

  const { results, count } = data;
  const paginationMax = ceil(count / FETCH_MY_BETS_LIMIT);
  const buttonIcon =
    ordering === "match__datetime" ? (
      <ArrowDownwardIcon />
    ) : (
      <ArrowUpwardIcon />
    );
  return (
    <Stack>
      <Stack direction="row" sx={{ justifyContent: "space-between" }}>
        {/* <Button size="small" onClick={toggleOrdering}>
          {buttonIcon} Bet made
        </Button> */}
        <Pagination
          sx={{ "& ul": { pt: "10px", pl: "30px" } }}
          count={paginationMax}
          page={page}
          onChange={handlePageChange}
        />
        <Button size="small" onClick={toggleOrdering}>
          {buttonIcon} Kick Off
        </Button>
      </Stack>
      {results.map((bet, i) => (
        <BetCard {...bet} key={`bet-${i}`} />
      ))}
    </Stack>
  );
};

export default BetsTabs;
