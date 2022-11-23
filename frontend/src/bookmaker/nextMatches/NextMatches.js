import React from "react";
import { Container } from "@mui/material";
import { useFetchNextMatchesQuery } from "../bookmakerApi";
import MatchCard from "./MatchCard";
import { Loading, Error } from "src/ui";

const NextMatches = () => {
  const { data, isLoading, isError } = useFetchNextMatchesQuery();

  return (
    <Container maxWidth="sm">
      {isLoading ? (
        <Loading />
      ) : isError ? (
        <Error />
      ) : (
        data.map((match) => (
          <MatchCard key={`match-${match.id}`} match={match} />
        ))
      )}
    </Container>
  );
};

export default NextMatches;
