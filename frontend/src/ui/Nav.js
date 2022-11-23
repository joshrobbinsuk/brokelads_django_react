import React, { useState } from "react";
import { useNavigate, useLocation } from "react-router-dom";
import {
  AppBar,
  Box,
  Container,
  Drawer,
  Hidden,
  IconButton,
  Stack,
  Toolbar,
  Typography,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import MenuIcon from "@mui/icons-material/Menu";
import useScrollPosition from "@react-hook/window-scroll";

import GradientBg from "./GradientBg";

const links = [
  { text: "MATCHES", url: "/" },
  { text: "BETS", url: "bets" },
  { text: "ACCOUNT", url: "account" },
];

const LinkBox = ({
  fontColor,
  hoverColor,
  scrollY,
  linkUrl,
  linkText,
  ...props
}) => {
  const navigate = useNavigate();
  const { pathname } = useLocation();
  const isThisPath =
    pathname.indexOf(linkUrl) > 0 || (pathname === "/" && linkUrl === "/");
  const borderBottom = isThisPath ? "2px solid" : "2px solid transparent";

  return (
    <Box
      onClick={() => navigate(`${linkUrl}`)}
      sx={{
        lineHeight: "30px",
        borderBottom: borderBottom,
        transition: "color 0.5s, border 0.5s ease",
        fontWeight: "700",
        fontSize: "12px",
        letterSpacing: "1.8px",
        textTransform: "uppercase",
        color: fontColor,
        "&:hover": {
          color: hoverColor,
          cursor: "pointer",
        },
      }}
      {...props}
    >
      <Typography variant="h3">{linkText}</Typography>
    </Box>
  );
};

const Nav = ({ navType, ...rest }) => {
  const scrollY = useScrollPosition(30);
  const [mobileOpen, setMobileOpen] = useState(false);

  // header customisation
  let fontColor = "darkGrey.main";
  let sideDrawerBgColor = "white.main";
  let hoverColor = "midGrey.main";
  if (navType && !scrollY) {
    fontColor = "white.main";
    sideDrawerBgColor = "midGrey.main";
    hoverColor = "midGrey.light";
  }

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  return (
    <AppBar
      position="fixed"
      sx={{
        background: "transparent",
        boxShadow: scrollY === 0 ? "none" : "0px 2px 4px -1px rgb(0 0 0 / 20%)",
      }}
    >
      {/* BAR */}
      <GradientBg scrollY={scrollY}>
        <Container maxWidth="lg">
          <Toolbar
            disableGutters={true}
            sx={{ justifyContent: "space-between" }}
          >
            <Box></Box>
            <Hidden smDown implementation="css">
              <Stack direction="row" sx={{ alignItems: "center" }}>
                {links.map(({ url, text }, i) => (
                  <LinkBox
                    key={`link-${url}`}
                    fontColor={fontColor}
                    hoverColor={hoverColor}
                    linkUrl={url}
                    linkText={text}
                    mx={2}
                  />
                ))}
              </Stack>
            </Hidden>
            <Hidden smUp>
              <Box onClick={handleDrawerToggle}>
                <IconButton
                  aria-label="open drawer"
                  sx={{
                    "& svg": {
                      color: fontColor,
                      transition: "color 0.5s",
                    },
                  }}
                >
                  <MenuIcon />
                </IconButton>
              </Box>
            </Hidden>
          </Toolbar>
        </Container>
      </GradientBg>

      {/* DRAWER */}
      <Hidden smUp implementation="js">
        <Drawer
          variant="temporary"
          anchor="right"
          open={mobileOpen}
          onClose={handleDrawerToggle}
        >
          <Box sx={{ backgroundColor: sideDrawerBgColor, height: "100%" }}>
            <Stack sx={{ justifyContent: "center" }} p={2}>
              <Stack onClick={handleDrawerToggle} my={4}>
                {links.map(({ url, text }, i) => (
                  <LinkBox
                    key={`link-${url}`}
                    fontColor={fontColor}
                    hoverColor={hoverColor}
                    linkUrl={url}
                    linkText={text}
                    my={1}
                  />
                ))}
                <LinkBox
                  fontColor={fontColor}
                  hoverColor={hoverColor}
                  my={2}
                ></LinkBox>
              </Stack>
              <Box>
                <IconButton
                  color="inherit"
                  aria-label="open drawer"
                  onClick={handleDrawerToggle}
                  sx={{
                    display: "block",
                    margin: "0 auto",
                    height: "40px",
                    "& svg": {
                      color: fontColor,
                      transition: "color 0.5s",
                    },
                  }}
                >
                  <CloseIcon />
                </IconButton>
              </Box>
            </Stack>
          </Box>
        </Drawer>
      </Hidden>
    </AppBar>
  );
};

export default Nav;
