import { Box } from "@mui/material";

const GradientBg = ({ scrollY, children }) => (
  <Box
    sx={{
      background: `linear-gradient(
        208.12deg,
              #ffffff -10.42%,
              #ede4e4 13.73%,
              #dbc8c8 39.65%,
              #e57373 94.01%

      )`,
      transition: "opacity 0.5s",
      opacity: scrollY === 0 ? 1 : 0,
      position: "absolute",
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
    }}
  >
    {children}
  </Box>
);

export default GradientBg;
