import React from "react";
import { Typography, Stack, Box } from "@mui/material";

import moment from "moment";
const MatchRow = ({
  homeTeam,
  homeTeamLogo,
  awayTeam,
  awayTeamLogo,
  datetime,
}) => {
  const ukDatetime = moment(datetime).format("lll");
  return (
    <Stack width="100%">
      <Stack sx={{ alignItems: "center" }}>
        <Typography>{ukDatetime}</Typography>
      </Stack>
      <Stack direction="row" sx={{ justifyContent: "space-between" }}>
        <Team teamName={homeTeam} teamImg={homeTeamLogo} />
        <Typography sx={{ position: "relative", top: "8px" }}>v</Typography>
        <Team teamName={awayTeam} teamImg={awayTeamLogo} home={false} />
      </Stack>
    </Stack>
  );
};

const Team = ({ teamName, teamImg, home = true }) => {
  const direction = home ? "row" : "row-reverse";
  return (
    <Stack
      direction={direction}
      sx={{ width: "50%", justifyContent: "space-around" }}
    >
      <Box
        sx={{
          maxHeight: [30, 40],
          maxWidth: [30, 40],
          // mr: home ? 2 : 10,
          // ml: home ? 10 : 2,
        }}
      >
        {teamImg ? (
          <img
            style={{
              maxHeight: "100%",
              width: "auto",
              // border: "0.5px solid black",
            }}
            src={teamImg}
            alt={`${teamName} logo`}
          />
        ) : null}
      </Box>
      <TextElement text={teamName} />
    </Stack>
  );
};

const TextElement = ({ text }) => (
  <Stack sx={{ justifyContent: "center" }}>
    <Typography variant="body2">{text}</Typography>
  </Stack>
);

export default MatchRow;
