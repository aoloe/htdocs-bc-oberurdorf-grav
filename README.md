# Grav for bc-oberurdorf.ch

This is a metarepository for the Grav based website for the BC Oberurdorf.

For a full install you need:

- Grav
- the `bcoberurdorf-quark` theme
- the following plugins
  - lightslider (standard plugin)
  - events-ics (my github)
  - events-schedule (my github)

- Basic install as of impagina.org (i should take it out of there)

## Setup

- download Grav and put it in the `grav` directory at the root of the web server.
- remove the `grav/user/` directory
- get <https://github.com/aoloe/htdocs-bc-oberurdorf-grav> as `grav/user/`
- create the `grav/user/config/security.yaml` file and fill fill the salt value
- create the `accounts/`, `plugins/`, and `themes/` directory

- add the `events-schedule` plugin
- add the `events-ics` plugin, copy it's `events-ics.yaml` to `user/config/plugins/` and customize the `route` to `bc-oberurdorf.ics`.

## Creating the `events-schedule` plugin

- make sure that the cache is writable
- follow <https://learn.getgrav.org/plugins/plugin-tutorial> for creating the plugin.
- for now, only do `onPageContentRaw` when the plugin is active on the given page.
- read the `yaml` file from the plugin's `data` directory.
- create a modular template called `events-schedule.md`
  - `blueprints/pages/modular/events-schedule-next.yaml`
     - we probably have to define `public function onGetPageBlueprints(Event $event)` if we want it to work in the admin (cf. the _lightslider_ plugin).
  - `templates/modular/events-schedule-next.html.twig`
  - enable `onTwigTemplatePaths` in `onPluginsInitialized`
  - add the plugin's template directory in `onTwigTemplatePaths`
  - for the localized dates, i need to get grav to read the right file in `system/languages`:
    - set `default_lang: de` in `config/site.yaml`
    - and in `config/system.yaml` set:

        ```yaml
        languages:
          translations: true
          supported:
            - de
        ```
    - you can now get the month name with:

      ```php
      $language = Grav::instance()['language'];
      dump($language->translate('MONTHS_OF_THE_YEAR', null, true));
      ```

      where `public function translate($args, array $languages = null, $array_support = false, $html_out = false)`.



## TODO:

- [x] get the mobile navigation on top of the slider:
  - https://github.com/getgrav/grav-plugin-lightslider/issues/34
- [ ] add a link for maps: `geo:0,0?q=my+street+address` where 0s are lat and long (https://en.wikipedia.org/wiki/Geo_URI_scheme)
- [ ] write the text for the Schnuppertrainng
- [x] write the footer.
- [x] create the ical
