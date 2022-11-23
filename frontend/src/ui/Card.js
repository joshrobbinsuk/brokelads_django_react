import React from "react";
import { Card } from "@mui/material";
import { useTheme } from "@mui/material/styles";

const StyledCard = ({ children, extraPadding }) => {
  const theme = useTheme();
  const pb = extraPadding ? 1 : 0;
  return (
    <Card
      sx={{
        pb: pb,
        backgroundColor: theme.palette.white.main,
        mb: 4,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
      }}
    >
      {children}
    </Card>
  );
};

export default StyledCard;
