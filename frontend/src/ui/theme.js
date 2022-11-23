import { createTheme } from "@mui/material/styles";

const {
  palette: { augmentColor },
} = createTheme();

const red = "#e57373";
const whiteRed = "#ffebee";
const lightRed = "#ffcdd2";
const fadedRed = "#ef9a9a";
const midGrey = "#566777";
const darkGrey = "#1C1E1E";
const white = "#FFFFFF";

const colors = {
  red: {
    main: red,
  },
  whiteRed: {
    main: whiteRed,
  },
  lightRed: {
    main: lightRed,
  },
  fadedRed: {
    main: fadedRed,
  },
  midGrey: {
    main: midGrey,
  },
  darkGrey: {
    main: darkGrey,
  },
  white: {
    main: white,
  },
};

const extendedPalette = Object.keys(colors).reduce((palette, colorName) => {
  return {
    ...palette,
    [colorName]: augmentColor({ color: colors[colorName] }),
  };
}, {});

const spacing = 8;

export const lightTheme = createTheme({
  maxWidth: 1280,
  components: {
    MuiCssBaseline: {
      styleOverrides: {
        body: {
          background: `linear-gradient(203.27deg, ${colors.white.main} -26.2%, ${colors.lightRed.main} 2.05%, ${colors.lightRed.main} 32.39%, ${colors.red.main} 96.01%)`,
          backgroundRepeat: "no-repeat",
          backgroundAttachment: "fixed",
          "& .amplify-tabs-item[data-state=active]": {
            color: colors.red.main,
            borderColor: colors.red.main,
          },
          "& .amplify-button": { backgroundColor: colors.red.main },
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: 10,
          padding: spacing * 2,
          boxShadow: "none !important",
          boxSizing: "border-box",
        },
      },
    },
    MuiCard: {
      styleOverrides: {
        root: {
          background: "rgba(255, 255, 255, 0.7)",
        },
      },
    },
    MuiFormControl: {
      styleOverrides: {
        root: {
          marginTop: 10,
          color: colors.fadedRed.main,
          "& legend, & .MuiInputLabel-root": {
            color: `${colors.fadedRed.main} !important`,
          },
          "& .MuiFormLabel-colorSecondary": {
            color: `${colors.darkGrey.main} !important`,
          },
        },
      },
    },
    MuiTab: {
      styleOverrides: {
        root: {
          color: colors.darkGrey.main,
        },
      },
    },
    MuiPaper: {
      defaultProps: {
        elevation: 0,
      },
      styleOverrides: {
        root: {
          borderRadius: 8,
        },
      },
    },
    MuiInput: {
      styleOverrides: {
        root: {
          color: colors.midGrey.main,
          "&.Mui-disabled .MuiOutlinedInput-input": {
            color: colors.midGrey.main,
          },
        },
      },
    },
    MuiOutlinedInput: {
      styleOverrides: {
        root: {
          // color: colors.midGrey.main,
          background: "rgba(255, 255, 255, 0.2)",
          "&:hover .MuiOutlinedInput-notchedOutline": {
            borderColor: colors.fadedRed.main,
          },
          "&.Mui-disabled .MuiOutlinedInput-notchedOutline": {
            borderColor: colors.fadedRed.main,
          },

          "& .MuiOutlinedInput-notchedOutline, &.Mui-focused .MuiOutlinedInput-notchedOutline":
            {
              borderColor: colors.fadedRed.main,
            },
        },
      },
    },
  },
  palette: {
    primary: colors.darkGrey,
    secondary: colors.white,
    text: {
      primary: colors.darkGrey.main,
      secondary: colors.white.main,
    },
    ...extendedPalette,
  },
  shape: {
    borderRadius: 10,
  },
  spacing,
  typography: {
    fontFamily: "'Mr Eaves Mod', sans-serif",
    button: {
      fontWeight: 900,
      fontSize: "1rem",
      letterSpacing: "0.15rem",
    },
    h1: {
      fontSize: "1.75rem",
      fontWeight: 500,
      marginBottom: spacing * 3,
    },
    h2: {
      fontSize: "1.65rem",
      fontWeight: 500,
      marginBottom: spacing * 3,
    },
    h3: {
      fontSize: "1.55rem",
      fontWeight: "normal",
      marginBottom: spacing,
    },
    h4: {
      fontSize: "1.5rem",
      fontWeight: 500,
      marginBottom: spacing * 0.5,
    },
    h5: {
      fontSize: "1.5rem",
      fontWeight: 500,
      marginBottom: spacing * 0.5,
    },
    h6: {
      fontSize: "1.5rem",
      fontWeight: 500,
      marginBottom: spacing,
    },
    subtitle1: {
      fontSize: "1.2rem",
      fontWeight: 700,
      marginBottom: spacing,
    },
    subtitle2: {
      fontSize: "1rem",
      fontWeight: 700,
      marginBottom: spacing,
    },
    body1: {
      fontSize: "0.85rem",
      fontWeight: 400,
      lineHeight: 1.66,
    },
    body2: {
      fontSize: "1.15rem",
      fontWeight: 350,
    },
    caption: {
      fontSize: "1.1rem",
      fontWeight: 900,
      lineHeight: 1.66,
    },
  },
});
