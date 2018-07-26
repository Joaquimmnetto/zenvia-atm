import math

class BankNoteManager():


    def sort_notes(self, value, available_notes):
        """
        Sorts the correct bank notes to be given to the user withdrawing `value`, in order to minimize que ammount of notes given.

        Arguments:
        value -- Value to be withdrawn from the ATM
        available_notes -- list of integers containing the value of the notes available in this ATM

        Returns:
        A dict with all elements of available_notes in its keys, and the ammount of each available note needed for the withdrawn in its values.

        Raises:
        ValueError if the given value can't be withdrawn with the notes on available_notes
        """
        #This whole thing could be recursive, but it does not make for great reading, so I'm implementing the iterative way.
        result = {}
        current_value = value
        sorted_notes = sorted(available_notes, reverse=True)
        for note in sorted_notes:
            notes_needed = math.floor(current_value/note)
            current_value = current_value % note
            result[note] = notes_needed

        if not current_value == 0:
            raise ValueError("Can't form {} out of {}".format(value, available_notes))

        return result

