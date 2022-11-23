import React, { useState } from "react";
import { Tabs, Tab, Box, Container } from "@mui/material";

import BetsTabs from "./BetsTabs";
import { useFetchMyBetsQuery } from "../bookmakerApi";

const MyBets = () => {
  const [tabValue, setTabValue] = useState("UNDECIDED");
  const [page, setPage] = useState(1);
  const [ordering, setOrdering] = useState("match__datetime");

  const handleTabChange = (event, value) => {
    setTabValue(value);
    setPage(1);
    setOrdering("match__datetime");
  };

  const handlePageChange = (event, value) => {
    setPage(value);
  };

  const toggleOrdering = () => {
    setPage(1);
    if (ordering === "match__datetime") {
      setOrdering("-match__datetime");
    } else {
      setOrdering("match__datetime");
    }
  };

  const betsQuery = useFetchMyBetsQuery({
    page: page - 1,
    outcome: tabValue,
    ordering,
  });

  return (
    <Container maxWidth="sm">
      <Tabs value={tabValue} onChange={handleTabChange} variant="fullWidth">
        <Tab value="WON" label="Won" />
        <Tab value="LOST" label="Lost" />
        <Tab value="UNDECIDED" label="To play" />
      </Tabs>
      {/* <SwitchFadeTransition switchKey={tabValue}> */}
      <BetsTabs
        betsQuery={betsQuery}
        page={page}
        handlePageChange={handlePageChange}
        toggleOrdering={toggleOrdering}
        ordering={ordering}
        tabValue={tabValue}
      />
    </Container>
  );
};

export default MyBets;
