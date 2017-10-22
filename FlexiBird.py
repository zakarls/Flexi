def rotate_lines(self, deg=-90):
    """ Rotate self.polylines the given angle about their centers. """
    theta = radians(deg)  # Convert angle from degrees to radians
    cosang, sinang = cos(theta), sin(theta)

    for pl in self.polylines:
        # Find logical center (avg x and avg y) of entire polyline
        n = len(pl.lines)*2  # Total number of points in polyline
        cx = sum(sum(line.get_xdata()) for line in pl.lines) / n
        cy = sum(sum(line.get_ydata()) for line in pl.lines) / n

        for line in pl.lines:
            # Retrieve vertices of the line
            x1, x2 = line.get_xdata()
            y1, y2 = line.get_ydata()

            # Rotate each around whole polyline's center point
            tx1, ty1 = x1-cx, y1-cy
            p1x = ( tx1*cosang + ty1*sinang) + cx
            p1y = (-tx1*sinang + ty1*cosang) + cy
            tx2, ty2 = x2-cx, y2-cy
            p2x = ( tx2*cosang + ty2*sinang) + cx
            p2y = (-tx2*sinang + ty2*cosang) + cy

            # Replace vertices with updated values
            pl.set_line(line, [p1x, p2x], [p1y, p2y])
