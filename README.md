# V-Dashboard

Dashboard starter template built with Vite, Vue 3, Tailwind CSS and TypeScript.

Copied from https://github.com/tailwindcomponents/dashboard and converted to Vue.

## Demo

https://v-dashboard.vercel.app/

![Demo](https://i.imgur.com/RqXxEHL.gif)

Note if you have access to [Tailwind UI](https://tailwindui.com), you can follow the following steps to add it:

1. Install `@tailwindcss/ui`:

```sh
yarn add @tailwindcss/ui
```

2. Add the plugin in `tailwind.config.js` without changing anything else:

```js
// tailwind.config.js
module.exports = {
  // ...
  // rest of the config
  plugins: [require('@tailwindcss/ui')],
}
```

## Project setup
```
yarn
```

### Compiles and hot-reloads for development
```
yarn dev
```

### Compiles and minifies for production
```
yarn build
```

## License & copyright

Licensed under the [MIT License](LICENSE.md).
