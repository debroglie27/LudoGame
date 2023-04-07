class Path:
    def __init__(self):
        red_path_list = [(210, 504), (210, 472), (210, 440), (210, 408), (210, 376),  # R Main
                         (175, 341), (143, 341), (111, 341), (79, 341), (47, 341),    # RG Main
                         (15, 341), (15, 301), (15, 261),                             # G Short
                         (47, 261), (79, 261), (111, 261), (143, 261), (175, 261),    # G Main
                         (210, 225), (210, 193), (210, 161), (210, 129), (210, 97),   # GY Main
                         (210, 65), (250, 65), (290, 65),                             # Y Short
                         (290, 97), (290, 129), (290, 161), (290, 193), (290, 225),   # Y Main
                         (326, 261), (357, 261), (390, 261), (421, 261), (453, 261),  # YB Main
                         (485, 261), (485, 301), (485, 341),                          # B Short
                         (453, 341), (421, 341), (390, 341), (357, 341), (326, 341),  # B Main
                         (290, 376), (290, 408), (290, 440), (290, 472), (290, 504),  # BR Main
                         (290, 535), (250, 535),                                      # R Short
                         (250, 504), (250, 472), (250, 440), (250, 408), (250, 376), (250, 340)]  # Red Home

        green_path_list = [(47, 261), (79, 261), (111, 261), (143, 261), (175, 261),    # G Main
                           (210, 225), (210, 193), (210, 161), (210, 129), (210, 97),   # GY Main
                           (210, 65), (250, 65), (290, 65),                             # Y Short
                           (290, 97), (290, 129), (290, 161), (290, 193), (290, 225),   # Y Main
                           (326, 261), (357, 261), (390, 261), (421, 261), (453, 261),  # YB Main
                           (485, 261), (485, 301), (485, 341),                          # B Short
                           (453, 341), (421, 341), (390, 341), (357, 341), (326, 341),  # B Main
                           (290, 376), (290, 408), (290, 440), (290, 472), (290, 504),  # BR Main
                           (290, 535), (250, 535), (210, 535),                          # R Short
                           (210, 504), (210, 472), (210, 440), (210, 408), (210, 376),  # R Main
                           (175, 341), (143, 341), (111, 341), (79, 341), (47, 341),    # RG Main
                           (15, 341), (15, 301),                                        # G Short
                           (47, 301), (79, 301), (111, 301), (143, 301), (175, 301), (211, 301)]    # Green Home

        yellow_path_list = [(290, 97), (290, 129), (290, 161), (290, 193), (290, 225),   # Y Main
                            (326, 261), (357, 261), (390, 261), (421, 261), (453, 261),  # YB Main
                            (485, 261), (485, 301), (485, 341),                          # B Short
                            (453, 341), (421, 341), (390, 341), (357, 341), (326, 341),  # B Main
                            (290, 376), (290, 408), (290, 440), (290, 472), (290, 504),  # BR Main
                            (290, 535), (250, 535), (210, 535),                          # R Short
                            (210, 504), (210, 472), (210, 440), (210, 408), (210, 376),  # R Main
                            (175, 341), (143, 341), (111, 341), (79, 341), (47, 341),    # RG Main
                            (15, 341), (15, 301), (15, 261),                             # G Short
                            (47, 261), (79, 261), (111, 261), (143, 261), (175, 261),    # G Main
                            (210, 225), (210, 193), (210, 161), (210, 129), (210, 97),   # GY Main
                            (210, 65), (250, 65),                                        # Y Short
                            (250, 97), (250, 129), (250, 161), (250, 193), (250, 225), (250, 261)]   # Yellow Home

        blue_path_list = [(453, 341), (421, 341), (390, 341), (357, 341), (326, 341),  # B Main
                          (290, 376), (290, 408), (290, 440), (290, 472), (290, 504),  # BR Main
                          (290, 535), (250, 535), (210, 535),                          # R Short
                          (210, 504), (210, 472), (210, 440), (210, 408), (210, 376),  # R Main
                          (175, 341), (143, 341), (111, 341), (79, 341), (47, 341),    # RG Main
                          (15, 341), (15, 301), (15, 261),                             # G Short
                          (47, 261), (79, 261), (111, 261), (143, 261), (175, 261),    # G Main
                          (210, 225), (210, 193), (210, 161), (210, 129), (210, 97),   # GY Main
                          (210, 65), (250, 65), (290, 65),                             # Y Short
                          (290, 97), (290, 129), (290, 161), (290, 193), (290, 225),   # Y Main
                          (326, 261), (357, 261), (390, 261), (421, 261), (453, 261),  # YB Main
                          (485, 261), (485, 301),                                      # B Short
                          (453, 301), (421, 301), (390, 301), (357, 301), (326, 301), (290, 301)]  # Blue Home

        self.path_lists = [red_path_list, green_path_list, yellow_path_list, blue_path_list]
